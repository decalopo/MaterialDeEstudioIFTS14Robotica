#Creo matriz
A=[0,0,0,0,0];
#Declaración de Funciones

#Ingresamos los numeros
def ingresoNumeros(A):
    for ii in range(0,len(A)):
        x=int(input("Ingrese un numero"));
        A[ii]=x;
    print (A);
    z=input("PRESS TO ORDER");


#Aca ordenamos los valores ingresados 
def algoritmoOrdenamiento(A):
    for i in range(1,len(A)):
        for j in range(0,len(A)-i):
            if(A[j+1] < A[j]):
                aux=A[j];
                A[j]=A[j+1];
                A[j+1]=aux;
    print (A);
 
#Programa Principal

a=input("Algoritmo de orndenamiento, ingresasr 5 valores luego ordenarlos de menor a mayor.Press to star...");
ingresoNumeros(A);
algoritmoOrdenamiento(A);
b=input("fin");


