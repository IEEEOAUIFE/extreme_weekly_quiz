package com.codesgenius;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int maxPos = -1, minPos = -1;

        int inputs = scan.nextInt();
        int data[] = new int[inputs];

        int max = Integer.MIN_VALUE;
        int min = Integer.MAX_VALUE;
        int shortest = Integer.MAX_VALUE;

        for(int i = 0; i < inputs; i++) {
            data[i] = scan.nextInt();
            max = Math.max(data[i], max);
            min = Math.min(data[i], min);
        }

        for(int i = 0; i < inputs; i++){
            if(data[i] == min){
                minPos = i;
            }
            if(data[i] == max){
                maxPos = i;
            }
            if(maxPos != -1 && minPos != -1){
                shortest = Math.min(shortest, (Math.abs(maxPos-minPos)+1));
            }
        }

        System.out.println(shortest);
    }
}
