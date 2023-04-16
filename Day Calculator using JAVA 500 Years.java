package com.company;
import java.awt.Desktop;
import java.net.URI;
import java.util.Scanner;
public class Calendar{
    public static void main(String[] args)
            throws Exception
    {
        System.out.println("Written by HARISHANKAR VASHISHTHA :)");
        Scanner sc = new Scanner(System.in);
        int Date;
        int Month=0;
        int Century=0;
        int TwoDigitOfYear=0;
        int ModBy4ofYear=0;
        int LeapYear=0;
        int Sum;
        int ModBy7ofSum;
        int Final;
        String Day="day";
        String MonthName="Error!";
        boolean ErrorInDate=true;
        boolean ErrorInMonth=true;
        boolean ErrorInYear=true;
        boolean CheckLeapYear=false;
        System.out.println("Your Date");
        int D=sc.nextInt();
        System.out.println("Your Month");
        int M=sc.nextInt();
        System.out.println("Your Year");
        int Y=sc.nextInt();
        if((M>12 || M==1) && (D>31 || D<1)){
            if(M==1 && (D>31 || D<1 )){
                System.out.println("Error in Date! \nProvide correct Date!");
                if(M>=1 && M<=12){
                    System.out.println("Error Reason:- January has only 31 days");
                }
            }
            if(M>12 && (D>31 || D<1)){
                System.out.println("Error in Date! \nProvide correct Date!");
                System.out.println("Error Reason :- Both Date and Month are Invalid!");
            }
        }
        else if(M==2 && D>28 || D<1) {
            if(D==29 && Y%4==0){
                CheckLeapYear=true;
                ErrorInDate = false;
            }
            else{
                System.out.println("\nError in Date! \nProvide correct Date!");
                System.out.println("February has only maximum 29 days!");
            }
        }
        else if(M==3 && D>31 || D<1) {
            System.out.println("\nError in Date! \nProvide correct Date!");
            System.out.println("Error Reason:- March has only 31 days");
        }
        else if(M==4 && D>30 || D<1) {
            System.out.println("\nError in Date! \nProvide correct Date!");
            System.out.println("Error Reason:- April has only 30 days");
        }
        else if(M==5 && D>31 || D<1) {
            System.out.println("\nError in Date! \nProvide correct Date!");
            System.out.println("Error Reason:- May has only 31 days");
        }
        else if(M==6 && D>30 || D<1) {
            System.out.println("\nError in Date! \nProvide correct Date!");
            System.out.println("Error Reason:- June has only 30 days");
        }
        else if(M==7 && D>31 || D<1) {
            System.out.println("\nError in Date! \nProvide correct Date!");
            System.out.println("Error Reason:- July has only 31 days");
        }
        else if(M==8 && D>31 || D<1) {
            System.out.println("\nError in Date! \nProvide correct Date!");
            System.out.println("Error Reason:- August has only 31 days");
        }
        else if(M==9 && D>30 || D<1) {
            System.out.println("\nError in Date! \nProvide correct Date!");
            System.out.println("Error Reason:- September has only 30 days");
        }
        else if(M==10 && D>31 || D<1) {
            System.out.println("\nError in Date! \nProvide correct Date!");
            System.out.println("Error Reason:- October has only 31 days");
        }
        else if(M==11 && D>30 || D<1) {
            System.out.println("\nError in Date! \nProvide correct Date!");
            System.out.println("Error Reason:- November has only 30 days");
        }
        else if(M==12 && D>31 || D<1) {
            System.out.println("\nError in Date! \nProvide correct Date!");
            System.out.println("Error Reason:- December has only 31 days");
        }
        else{
            ErrorInDate = false;
        }
        if(M<1 || M>12){
            System.out.println("\nError in Month! \nProvide correct Month!");
            System.out.println("Error Reason:- There are only 12 months in a year");
        }
        else{
            ErrorInMonth = false;
        }
        if(Y<1800 || Y>2299){
            System.out.println("\nError in Year! \nProvide correct Year!");
            System.out.println("Error Reason:- This program is made only from 1800 A.D to 2299 A.D ");
        }
        else{
            ErrorInYear = false;
        }
        switch(M){
            case 1:
                Month=1;
                MonthName="January";
                break;
            case 2:
                Month=4;
                MonthName="February";
                break;
            case 3:
                Month=4;
                MonthName="March";
                break;
            case 4:
                Month=0;
                MonthName="April";
                break;
            case 5:
                Month=2;
                MonthName="May";
                break;
            case 6:
                Month=5;
                MonthName="June";
                break;
            case 7:
                Month=0;
                MonthName="July";
                break;
            case 8:
                Month=3;
                MonthName="August";
                break;
            case 9:
                Month=6;
                MonthName="September";
                break;
            case 10:
                Month=1;
                MonthName="October";
                break;
            case 11:
                Month=4;
                MonthName="November";
                break;
            case 12:
                Month=6;
                MonthName="December";
                break;
        }
        if(Y>=1800 && Y<=1899){
            Century=2;
            TwoDigitOfYear=Y-1800;
            ModBy4ofYear=TwoDigitOfYear/4;
            if(Y%4==0 && (M==1 || M==2)){
                LeapYear=-1;
                if(Y==1800 || Y==1900 || Y==2100 || Y==2200){
                    LeapYear=0;
                }
            }
        }
        else if(Y>=1900 && Y<=1999){
            Century=0;
            TwoDigitOfYear=Y-1900;
            ModBy4ofYear=TwoDigitOfYear/4;
            if(Y%4==0 && (M==1 || M==2)){
                LeapYear=-1;
                if(Y==1800 || Y==1900 || Y==2100 || Y==2200){
                    LeapYear=0;
                }
            }
        }
        else if(Y>=2000 && Y<=2099){
            Century=6;
            TwoDigitOfYear=Y-2000;
            ModBy4ofYear=TwoDigitOfYear/4;
            if(Y%4==0 && (M==1 || M==2)){
                LeapYear=-1;
                if(Y==1800 || Y==1900 || Y==2100 || Y==2200){
                    LeapYear=0;
                }
            }
        }
        else if(Y>=2100 && Y<=2199){
            Century=4;
            TwoDigitOfYear=Y-2100;
            ModBy4ofYear=TwoDigitOfYear/4;
            if(Y%4==0 && (M==1 || M==2)){
                LeapYear=-1;
                if(Y==1800 || Y==1900 || Y==2100 || Y==2200){
                    LeapYear=0;
                }
            }
        }
        else if(Y>=2200 && Y<=2299){
            Century=2;
            TwoDigitOfYear=Y-2200;
            ModBy4ofYear=TwoDigitOfYear/4;
            if(Y%4==0 && (M==1 || M==2)){
                LeapYear=-1;
                if(Y==1800 || Y==1900 || Y==2100 || Y==2200){
                    LeapYear=0;
                }
            }
        }
        Date=D;
        Sum=(Date+Month+TwoDigitOfYear+ModBy4ofYear+Century+LeapYear);
        ModBy7ofSum=Sum%7;
        Final=ModBy7ofSum;
        switch(Final){
            case 1:
                Day="Sunday";
                break;
            case 2:
                Day="Monday";
                break;
            case 3:
                Day="Tuesday";
                break;
            case 4:
                Day="Wednesday";
                break;
            case 5:
                Day="Thursday";
                break;
            case 6:
                Day="Friday";
                break;
            case 0:
                Day="Saturday";
                break;
        }
        if(Y==1800 || Y==1900 || Y==2100 || Y==2200){
            if(M==2 && D>28 || D<1){
                ErrorInDate=true;
                System.out.println("\nError in Date! \nProvide correct Date!");
                System.out.println("Error Reason:- "+Y+" is not a Leap Year");
                System.out.println("Hence, February has only 28 days in Year "+Y);
            }
        }
        if(ErrorInDate==false && ErrorInMonth==false && ErrorInYear==false ) {
            System.out.println("\nThe day on " + Date + "/" + MonthName + "/" + Y + " is :- " + Day);
            System.out.println("*******************************************************");
            System.out.println("Thanks a lot!");
            System.out.println("I Hope you enjoyed this!");
            System.out.println("Harishankar Vashishtha wishes you all the best for your bright future.");
            System.out.println("    :This Calendar is designed by ~Harishankar Vashishtha");
            System.out.println("Type 1 to visit my website,there you can rate my code!");
            Scanner sc1 = new Scanner(System.in);
            int YesNo = sc1.nextInt();
            if (YesNo==1) {
                System.out.println("Website Opened :)");
                Desktop desk = Desktop.getDesktop();
                desk.browse(new URI("https://bit.ly/3qNbxFc"));
            }
           else{
                System.out.println("ERROR CODE 69!");
            }
        }
        else{
            System.out.println("\nCome back and Re-Run this program with correct Input :) ");
            System.out.println("*******************************************************");
        }
    }
}
