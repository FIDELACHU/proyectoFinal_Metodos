import java.util.Scanner;

public class proyectoFinal {    //metodo-biseccion
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double x1, x0, xr, error, multi;
        String funcion;
        double fx1, fx0, fxr;
        
        System.out.println("Ingrese el valor de X1:");
        x1 = scanner.nextDouble();
        System.out.println("Ingrese el valor de X0:");
        x0 = scanner.nextDouble();

        xr = (x1 + x0) / 2;     //punto medio
        error = Math.abs((x1 - x0) / x1) * 100;
        System.out.println("Escribe la funcion f(x):");
        funcion = scanner.nextLine();       //recibir la funcion

        fx1 = eval(funcion, x1);            //se supone eval puede cnvertir la funcion a un valor numerico
        fx0 = eval(funcion, x0);
        fxr = eval(funcion, xr);

        multi = fxr * fx0;

        while (error > 0) {
            if (multi < 0) { // menor a 0 x1=xr
                x1 = xr;
                fx1 = eval(funcion, x1);
            } else { // mayor a 0 x0=xr
                x0 = xr;
                fx0 = eval(funcion, x0);
            }
            xr = (x1 + x0) / 2;     //recalcular el punto medio y el error %
            error = Math.abs((x1 - x0) / x1) * 100;
            fxr = eval(funcion, xr);
            multi = fxr * fx0;
        }
    }
}