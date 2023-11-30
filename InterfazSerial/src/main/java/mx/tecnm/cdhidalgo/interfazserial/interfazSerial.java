/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package mx.tecnm.cdhidalgo.interfazserial;
import com.fazecast.jSerialComm.SerialPort;
/**
 *
 * @author josec
 */
public class interfazSerial {
    public static void main(String[] args) {
        System.out.println("Puertos disponibles");
        System.out.println("");
        SerialPort [] puertos = SerialPort.getCommPorts();
        
        for (int i = 0; i < puertos.length; i++) {
            System.out.println(puertos[i].getSystemPortName());
        }
        
    }
}
