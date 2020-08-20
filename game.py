import os


class Board_to_play():

    def __init__(self):
        self.board=[" "," "," "," "," "," "," "," "," "]
    
    def display_board(self):
        print("          |          |           ")
        print("          |          |           ")
        print("  ",self.board[0],"     |","  ",self.board[1],"    |","   ",self.board[2])
        print("__________|__________|___________")
        print("          |          |           ")
        print("          |          |           ")
        print("  ",self.board[3],"     |","  ",self.board[4],"    |","   ",self.board[5])
        print("__________|__________|___________")
        print("          |          |           ")
        print("          |          |           ")
        print("  ",self.board[6],"     |","  ",self.board[7],"    |","   ",self.board[8])
        print("          |          |           ")
    
    def update_the_board(self, cell_num, player):
        if(self.board[cell_num]==" "):
            self.board[cell_num]=player
        
    

    def winner_of_the_game(self,player):
        if(self.board[0]==player and self.board[1]==player and self.board[2]==player):
            return True
        if(self.board[0]==player and self.board[1]==player and self.board[2]==player):
            return True 
        if(self.board[3]==player and self.board[4]==player and self.board[5]==player):
            return True 
        if(self.board[6]==player and self.board[7]==player and self.board[8]==player):
            return True 
        if(self.board[0]==player and self.board[4]==player and self.board[8]==player):
            return True 
        if(self.board[2]==player and self.board[4]==player and self.board[6]==player):
            return True 
        if(self.board[0]==player and self.board[3]==player and self.board[6]==player):
            return True 
        if(self.board[1]==player and self.board[4]==player and self.board[7]==player):
            return True 
        if(self.board[2]==player and self.board[5]==player and self.board[8]==player):
            return True

    def tie_game(self):
        boxes=0
        for i in self.board:
            if(i!=" "):
                boxes+=1
        if(boxes==9):
            return True  

    def position_not_free(self,cell_num,player):
        if(self.board[cell_num]!=" "):
            print("Sorry that space is not free,enter other position")
            return True
    
if __name__=="__main__":
    play=Board_to_play()

    def heading():
        #display_in_the_starting
        print("TIC-TAC-TOE GAME")
        print("\n")
        print("This is the position of the board")
        print("  1   |  2  |  3  ")
        print("______|_____|_____")
        print("  4   |  5  |  6  ")
        print("______|_____|_____")
        print("  7   |  8  |  9  ")
        print("LET'S START THE GAME :) \n")
        play.display_board()

    def heading_new():
    
    
        print("This is the position of the board")
        print("  1   |  2  |  3  ")
        print("______|_____|_____")
        print("  4   |  5  |  6  ")
        print("______|_____|_____")
        print("  7   |  8  |  9  ")
        print("LET'S START THE GAME :) \n")
        
    def refresh_screen():
        #clear the screen
        os.system("cls")
        #print_the_heading
        heading_new()
        #display_board
        play.display_board()

    heading()


    while True:
    
        #player_x
        print("PLAYER_X PLEASE ENTER THE NUMBER , WHERE YOU WANT TO MARK ON THE BOARD(1-9)")
        num=int(input())
        while num not in range(1,10):
            print("Sorry position is not on the board,enter again")
            num=int(input())
    
        if(play.position_not_free(num-1,"X")):
            num=int(input())
        play.update_the_board(num-1,"X")

        #refresh screen for the next player
        refresh_screen()

        #checking the winner
        if(play.winner_of_the_game("X")):
            print("\n Congratulations Player X","\n","YOU WON!!!") 
            break

        #checking for tie
        if(play.tie_game()):
            print("\n TIE!!")
            break

    

        #Player_O
        print("PLAYER_O PLEASE ENTER THE NUMBER , WHERE YOU WANT TO MARK ON THE BOARD(1-9)")
        num_1=int(input())
        while num_1 not in range(1,10):
            print("Sorry position is not on the board,enter again")
            num_1=int(input())
        if(play.position_not_free(num_1-1,"X")):
            num_1=int(input())
        play.update_the_board(num_1-1,"O")

        refresh_screen()

        #checking Player O
        if(play.winner_of_the_game("O")):
            print("\n Congratulations Player O","\n","YOU WON!!!")
            break 

        #checking for tie
        if(play.tie_game()):
            print("\n TIE!!")
            break
