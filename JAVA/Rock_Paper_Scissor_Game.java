import java.util.Scanner;
import java.util.Random;

public class RockPaperScissor {

    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        
        //User Input
        System.out.println("Make your choice! (ROCK/PAPER/SCISSOR)");
        String playerMove = scanner.nextLine();
        
        //Computer Input
        Random random = new Random();
        int RNG = random.nextInt(3);
        
        //Random Number Generator to decide computer's move
        String PC;
        if (RNG == 0){
            PC = "rock";
        }
        else if (RNG == 1){
            PC = "paper";
        }
        else if (RNG == 2){
            PC = "scissor";
        }
        
        System.out.println("The computer chose " + PC + "!");
        
        //Results
          if (playerMove.equals(PC)){
            System.out.println("It's a draw!");
        } else if (playerWins(playerMove, PC)){
            System.out.println("Player Wins!");
        } else {
            System.out.println("Computer Wins!");
        }
    }
    
    //Checks the result of the match
    static boolean playerWins(String playerMove, String PC){
        if (playerMove.equals("rock")){
            return PC.equals("scissor");
        } else if (playerMove.equals("paper")){
                return PC.equals("rock");
        } else{
                return PC.equals("paper");
            }
                
        }
        
      
    
}
