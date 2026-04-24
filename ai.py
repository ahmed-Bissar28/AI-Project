import tkinter as tk
import heapq

class State:
    def __init__(self, missionaries, cannibals, boat, parent=None):
        self.m = missionaries
        self.c = cannibals
        self.b = boat
        self.parent = parent
        self.cost = 0 if parent is None else parent.cost + 1

    def is_valid(self):
        if self.m < 0 or self.c < 0 or self.m > 3 or self.c > 3:
            return False
        if self.m > 0 and self.m < self.c:
            return False 
        if (3 - self.m) > 0 and (3 - self.m) < (3 - self.c):
            return False 
        return True

    def is_goal(self):
        return self.m == 0 and self.c == 0 and self.b == 0

    def __eq__(self, other):
        return self.m == other.m and self.c == other.c and self.b == other.b

    def __hash__(self):
        return hash((self.m, self.c, self.b))

    def __lt__(self, other):
        return self.cost < other.cost

class GameAI:
    @staticmethod
    def get_successors(state):
        successors = []
        moves = [(1, 0), (0, 1), (2, 0), (0, 2), (1, 1)]
        for m, c in moves:
            if state.b == 1:
                new_state = State(state.m - m, state.c - c, 0, state)
            else:
                new_state = State(state.m + m, state.c + c, 1, state)
                
            if new_state.is_valid():
                successors.append(new_state)
        return successors

    @staticmethod
    def a_star(initial_state):
        frontier = []
        heapq.heappush(frontier, (0, initial_state))
        explored = set()
        
        while frontier:
            _, state = heapq.heappop(frontier)
            if state.is_goal(): return state
            explored.add(state)
            
            for child in GameAI.get_successors(state):
                if child not in explored:
                    f_cost = child.cost + (child.m + child.c) 
                    heapq.heappush(frontier, (f_cost, child))
        return None

class MissionariesCannibalsUI:
    def __init__(self, root, path):
        self.root = root
        self.root.title("Missionaries and Cannibals - AI Solver")
        self.path = path
        self.current_step = 0

        self.canvas = tk.Canvas(root, width=800, height=400, bg="skyblue")
        self.canvas.pack(pady=20)

        self.btn_next = tk.Button(root, text="الخطوة التالية (Next Step)", font=("Arial", 14), command=self.next_step)
        self.btn_next.pack()

        self.lbl_status = tk.Label(root, text="Start", font=("Arial", 16))
        self.lbl_status.pack(pady=10)

        self.draw_state(self.path[self.current_step])

    def draw_state(self, state):
        self.canvas.delete("all")
        
        self.canvas.create_rectangle(0, 200, 250, 400, fill="forestgreen", outline="") 
        self.canvas.create_rectangle(550, 200, 800, 400, fill="forestgreen", outline="")  
        self.canvas.create_rectangle(250, 200, 550, 400, fill="dodgerblue", outline="") 

        for i in range(state.m): self.draw_person(50 + i*40, 150, "blue", "M")
        for i in range(state.c): self.draw_person(50 + i*40, 250, "red", "C")

        for i in range(3 - state.m): self.draw_person(600 + i*40, 150, "blue", "M")
        for i in range(3 - state.c): self.draw_person(600 + i*40, 250, "red", "C")

        boat_x = 260 if state.b == 1 else 440
        self.canvas.create_rectangle(boat_x, 220, boat_x + 100, 260, fill="saddlebrown")
        self.canvas.create_text(boat_x + 50, 240, text="Boat", fill="white", font=("Arial", 12, "bold"))

        self.lbl_status.config(text=f"Step: {self.current_step} / {len(self.path)-1}")

    def draw_person(self, x, y, color, label):
        self.canvas.create_oval(x, y, x+30, y+30, fill=color)
        self.canvas.create_text(x+15, y+15, text=label, fill="white", font=("Arial", 12, "bold"))

    def next_step(self):
        if self.current_step < len(self.path) - 1:
            self.current_step += 1
            self.draw_state(self.path[self.current_step])
            if self.current_step == len(self.path) - 1:
                self.lbl_status.config(text="Goal Reached!", fg="green")
                self.btn_next.config(state="disabled")

if __name__ == "__main__":
    initial_state = State(3, 3, 1)
    
    goal_state = GameAI.a_star(initial_state)
    
    if goal_state:
        path = []
        curr = goal_state
        while curr:
            path.append(curr)
            curr = curr.parent
        path.reverse()

        root = tk.Tk()
        app = MissionariesCannibalsUI(root, path)
        root.mainloop()
    else:
        print("No solution")