from rich.console import Console, ConsoleOptions, RenderResult
from rich.table import Table
from rich import print
from rich import box
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, transpile, Aer, execute
from qiskit.providers.aer import QasmSimulator
from qiskit.compiler import assemble
import asyncio
from azure.quantum.qiskit import AzureQuantumProvider

provider = AzureQuantumProvider (
    resource_id = "/subscriptions/b1d7f7f8-743f-458e-b3a0-3e09734d716d/resourceGroups/aq-hackathons/providers/Microsoft.Quantum/Workspaces/aq-hackathon-01",
    location = "eastus"
)

print([backend.name() for backend in provider.backends()])

backend = provider.get_backend('ionq.simulator')


class board:
    def __init__(self) -> None:
        self.board=[
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

        self.PlayerX_turn = True
        self.board_state={
            0: ' ',
            1: ' ',
            2: ' ',
            3: ' ',
            4: ' ',
            5: ' ',
            6: ' ',
            7: ' ',
            8: ' ',
        }

    async def q_measure(self):
        qr = QuantumRegister(9)
        cr = ClassicalRegister(9)
        qc = QuantumCircuit(qr, cr)

        temp_board = self.board_state
        while sum([len(cell_val) for cell_val in temp_board.values()]) > 0:
            # Apply H and X gates
            for i in range(9):
                cell_length = len(temp_board[i])
                for e in range(cell_length):
                    if e >= len(temp_board[i]) or temp_board[i][0] == '(':
                        break
                    elif temp_board[i][0] == '1':
                        qc.x(qr[i])
                        qc.h(qr[i])
                    elif temp_board[i][0] == '0':
                        qc.h(qr[i])
                    temp_board[i] = temp_board[i][1:]
            
            # Apply CX Gate
            for i in range(9):
                if len(temp_board[i]) == 0:
                    continue
                else:
                    if temp_board[i][:3] == '(CX':
                        cell0 = int(temp_board[i][3])
                        cell1 = int(temp_board[i][4])
                        qc.cx(qr[cell0], qr[cell1])
                        temp_board[cell0] = temp_board[i][6:]
                        temp_board[cell1] = temp_board[i][6:]

        qc.measure(qr, cr)

        print('\n', qc.draw(), '\n')

        job = backend.run(qc, shots=128)
        job_id = job.id()
        print(f'\nJob id: {job_id}')
        result = job.result()
        counts = result.get_counts()
        sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        top_count = sorted_counts[0][0][::-1]

        for i in range(9):
            if top_count[i] == '1':
                self.board_state[i] = "⭕"
            else:
                self.board_state[i] = "❌"
        # if '1' in counts.keys():
        #     self.board_state[key] = "⭕"
        # else:
        #     self.board_state[key] = "❌"

    def update_board(self):
        for i in range(3):
            for j in range(3):
                if self.board_state[i * 3 + j] == "❌":
                    self.board[i][j] = 1
                elif self.board_state[i * 3 + j] == "⭕":
                    self.board[i][j] = -1
                else:
                    self.board[i][j] = 0
    
    def win(self):
        self.update_board()
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return False

        if self.board_state[0] == self.board_state[1] == self.board_state[2] or self.board_state[0] == self.board_state[4] == self.board_state[8]\
            or self.board_state[0] == self.board_state[3] == self.board_state[6]:
                print(self)
                print("\n[center][green][bold]Game Over.\n")
                print(f"[green]{self.board_state[0]} WINS!")
                return True
        if self.board_state[1] == self.board_state[4] == self.board_state[7] or self.board_state[3] == self.board_state[4] == self.board_state[5]\
            or self.board_state[6] == self.board_state[4] == self.board_state[2]:
                print(self)
                print("\n[center][green][bold]Game Over.\n")
                print(f"[green]{self.board_state[4]} WINS!")
                return True
        if self.board_state[2] == self.board_state[5] == self.board_state[8] or self.board_state[6] == self.board_state[7] == self.board_state[8]:
                print(self)
                print("\n[center][green][bold]Game Over.\n")
                print(f"[green]{self.board_state[8]} WINS!")
                return True
        return False                 
               
    async def mes(self):
        for i in range(3):
            for j in range(3):
                if not (self.board[i][j] == 0 and self.board_state[i * 3 + j] != " "):
                    return
        await self.q_measure()
        self.update_board()
        # for i in range(3):
        #     for j in range(3):
        #         if self.board[i][j]==0 and self.board_state[i * 3 + j]!=" ":
        #             await self.q_measure(self.board_state[i * 3 + j],i * 3 + j)
        #             self.update_board()


    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult:
        table = Table(title="[green]Board", show_header=False, show_lines=True, border_style=None, box=box.ROUNDED)
        table.add_column(justify="center")
        table.add_column(justify="center")
        table.add_column(justify="center")
        table.add_row(self.board_state[0], self.board_state[1], self.board_state[2])
        table.add_row(self.board_state[3], self.board_state[4], self.board_state[5])
        table.add_row(self.board_state[6], self.board_state[7], self.board_state[8])
        yield table

        

if __name__=='__main__':
    board = board()

    print("[bold italic black on yellow blink]Welcome to Tic Tac Toe!\n")
    print("[bold italic green]Instructions:")
    print("1. X's turn applies an X and H gate on the\n   position.")
    print("2. O's turn applies a H gate on the position.")
    print("3. Select the cell to take your turn (0-8). A '1'\n   will be placed for X's turn and a '0' for O's\n   turn.")
    print("4. Players may take their turn on existing cells\n   to change its state.")
    print("5. When a player wants to use the current state\n   of the board to get results, they can measure it\n   with 'm'.")
    print("6. Have fun!\n")
    input("Press enter to continue...")
    print("\n")

    backend_choice = None
    while not backend_choice:
        backend_choice_text = " Please choose a quantum backend (1) for simulator, (2) for qpu: "
        print(f"[green]{backend_choice_text}")
        backend_choice = input(f"\033[1A \033[{len(backend_choice_text) - 1}C")
        if backend_choice == '1':
            backend = provider.get_backend('ionq.simulator')
        elif backend_choice == '2':
            backend = provider.get_backend('ionq.qpu')
        else:
            backend_choice = None
    
    print("\n\n\n\n")

    while not board.win():
        print('\n')
        if board.PlayerX_turn:
            print("[bold red]TURN: ❌")
        else:
            print("[bold red]TURN: ⭕")
        print(board)

        turn_text = " Enter the number of the cell you want to mark or 'CX (cell 1) (cell 2)' to entangle or 'M' to measure: "
        print(f"\n[green]{turn_text}")
        inp = input(f"\033[1A \033[{len(turn_text) - 1}C")
        if inp.lower() == "m":
            asyncio.run(board.mes())
            board.PlayerX_turn = not board.PlayerX_turn
        elif inp[0:2].lower() == "cx":
            inp_left = inp[3:]
            if len(inp_left) < 3:
                print('[red]Entanglement needs 2 specified cells.')
            else:
                cell0 = inp_left[0]
                cell1 = inp_left[2]
                if cell0 not in ['0','1','2','3','4','5','6','7','8'] or cell1 not in ['0','1','2','3','4','5','6','7','8']:
                    print('[red]Cells must be 0-8.')
                else:
                    cell0 = int(cell0)
                    cell1 = int(cell1)
                    board.board_state[cell0] += f"(CX{cell0}{cell1})"
                    board.board_state[cell1] += f"(CX{cell0}{cell1})"
                    board.PlayerX_turn = not board.PlayerX_turn
        elif inp in ['0','1','2','3','4','5','6','7','8']:
            cell = int(inp)
            if board.board[cell // 3][cell % 3] == 0:
                if board.PlayerX_turn:
                    board.board_state[cell] = board.board_state[cell] + "1"
                    board.PlayerX_turn = False
                else:
                    board.board_state[cell] = board.board_state[cell] + "0"
                    board.PlayerX_turn = True
            else:
                print("[red]This cell is already marked.")
        else:
            print('[red]Invalid Input.')

        
    
