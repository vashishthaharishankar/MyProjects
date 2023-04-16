package com.company;
import java.util.Objects;
import java.util.Scanner;
import java.util.Random;
import java.awt.Desktop;
import java.net.URI;
public class Game {
    public static void main(String[] args)
            throws Exception
    {
        System.out.println("Written by HARISHANKAR VASHISHTHA :)");
        System.out.print("Hello!\nWelcome in this Rock,Paper and Scissor Game!\n");
        Scanner sc=new Scanner(System.in);
        System.out.println("Type Your Outcome :- Rock,Paper or Scissor");
        String user=sc.nextLine();
        if (Objects.equals(user, "Rock") ){
            System.out.println("\nYou Selected:-\nRock");
        }
        else if (Objects.equals(user, "Paper") ){
            System.out.println("\nYou Selected:-\nPaper");
        }
        else if (Objects.equals(user, "Scissor")){
            System.out.println("\nYou Selected:-\nScissor");
        }
        else{
            System.out.println("Type correct input!\nERROR! ERROR! ERROR!\nERROR! ERROR!\nERROR!");
        }
        Random ran=new Random();
        int upperbound=3;
        int a=ran.nextInt(upperbound);
        if(a==0){
            System.out.println("\nComputer Selected:-\nRock\n");
        }
        else if(a==1){
            System.out.println("\nComputer Selected:-\nPaper\n");
        }
        else{
            System.out.println("\nComputer Selected:-\nScissor\n");
        }
        if (Objects.equals(user, "Rock") && a==0){
            System.out.println("Match is TIED!\nYou both selected same outcome (Rock)");
        }
        else if (Objects.equals(user, "Rock") && a==1){
            System.out.println("Computer won this Game!\nBecause Paper will cover your Rock");
        }
        else if(Objects.equals(user, "Rock")  && a==2){
            System.out.println("You Won this Game!\nBecause your Rock will damage Scissor");
        }
        else if (Objects.equals(user, "Paper") && a==0){
            System.out.println("You Won this Game!\nBecause your Paper will cover Rock");
        }
        else if(Objects.equals(user, "Paper") && a==1){
            System.out.println("Match is TIED!\nYou both selected same outcome (Paper)");
        }
        else if(Objects.equals(user, "Paper") && a==2){
            System.out.println("Computer Won this Game!\nBecause Scissor will cut your Paper");
        }
        else if(Objects.equals(user, "Scissor") && a==0){
            System.out.println("Computer Won this Game!\nBecause Rock will Damage your Scissor");
        }
        else if(Objects.equals(user, "Scissor") && a==1){
            System.out.println("You Won this Game!\nBecause your Scissor will cut Paper");
        }
        else if(Objects.equals(user, "Scissor") && a==2){
            System.out.println("Match is TIED!\nYou both selected same outcome (Scissor)");
        }
        else{
            System.out.println("Type correct input!");
            System.out.println("ERROR! ERROR! ERROR!\nERROR! ERROR!\nERROR!");
        }
        System.out.println("Thanks a lot!");
        System.out.println("I Hope you enjoyed this Game!");
        System.out.println("Harishankar Vashishtha wishes you all the best for your bright future.");
        System.out.println("    :This game is designed by ~Harishankar Vashishtha");
        System.out.println("Type 1 to visit my website,there you can rate my code!");
        Scanner sc1=new Scanner(System.in);
        int rate=sc1.nextInt();
        if(rate==1){
            System.out.println("Website Opened :)");
            Desktop desk = Desktop.getDesktop();
            desk.browse(new URI("https://bit.ly/3qNbxFc"));
        }
        else{
            System.out.println("ERROR CODE 69!");
        }
    }
}