package jarvis;

import java.awt.*;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;

import java.lang.Math;

public class Jarvis extends JFrame implements KeyListener{
    
    JPanel panel = new JPanel();
    JTextArea dialog = new JTextArea(20,50);
    JTextArea input = new JTextArea(2,50);
    JScrollPane scroll = new JScrollPane(dialog,JScrollPane.VERTICAL_SCROLLBAR_AS_NEEDED,JScrollPane.HORIZONTAL_SCROLLBAR_NEVER);
    
    String[][] chatBot = {
        //standard greetings
        {"hi","hello","hola","ola","howdy","yo","whats up","what's up","sup","hey"},
        {"hi","hello","hey","whats up","yo","shlama"},
        //question greetings
        {"how are you","how you doin","how you doing","what's up","whats up","hows it going","hows it goin","how's it going","how's it goin"},
        {"great","good","doing well","ok","doin well","doing ok","fine thanks"},
        //default
        {"stop talking nonsense!","could you repeat that please?"},
    };
    
    public Jarvis(){
        super("Chat Bot J.A.R.V.I.S.");
        setSize(640,400);
        setResizable(false);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        dialog.setEditable(false);
        input.addKeyListener(this);
                
        panel.add(scroll);
        panel.add(input);
        panel.setBackground(new Color(100,200,150));
        add(panel);
        
        setVisible(true);
    }//end Jarvis constructor
    
    public static void main(String[] args) {
        new Jarvis();
    }//end MAIN
    
    public void addText(String str){
        dialog.setText(dialog.getText()+str);
    }//end AddText
    
    public boolean inArray(String in, String[] str){
        boolean match = false;
        for(int i = 0;i < str.length;i++){
           if(str[i].equals(in)){
               match = true;
           } 
        }
        return match;
    }//end inArray
        
    @Override
    public void keyTyped(KeyEvent e) {}//end keyTyped
    
    @Override
    public void keyPressed(KeyEvent e) {
        if (e.getKeyCode() == KeyEvent.VK_ENTER){
            input.setEditable(false);
            //---grab quote---//
            String quote = input.getText();
            input.setText("");
            addText("-->You:\t"+quote);
            quote.trim();
            while(
                    quote.charAt(quote.length() - 1)=='!' ||
                    quote.charAt(quote.length() - 1)=='.' ||
                    quote.charAt(quote.length() - 1)=='?'
                    ){
                quote = quote.substring(0,quote.length() - 1);
            }
            quote = quote.trim();
            //---check for match---//
            byte response = 0;
            /*
            0: searching thru chatBot array for match
            1: didnt find
            2: did find
            */
            int j = 0;//which group we check
            while(response == 0){
                if(inArray(quote.toLowerCase(),chatBot[j*2])){
                    response = 2;
                    int r = (int)Math.floor(chatBot[((j*2)+1)].length * Math.random());
                    addText("\n-->J.A.R.V.I.S.\t"+chatBot[(j*2)+1][r]);
                }
                j++;
                if ((j*2) == chatBot.length - 1 && response==0){
                    response = 1;
                }
            }
            
            //---no match go default---//
            if (response == 1){
                int r = (int)Math.floor(chatBot[chatBot.length-1].length * Math.random());
                addText("\n-->J.A.R.V.I.S.\t"+chatBot[chatBot.length-1][r]);
            }
            addText("\n");
        }
    }//end keyPressed

    @Override
    public void keyReleased(KeyEvent e) {
        if (e.getKeyCode() == KeyEvent.VK_ENTER){
            input.setEditable(true);
        }
    }//end keyReleased
   
}//end Jarvis
