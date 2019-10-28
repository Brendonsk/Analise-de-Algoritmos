#include "stdafx.h"
#include "LSE.h"
#include "LDE.h"
#include "Fila.h"

using namespace std;

struct grafo
{
    LSE *Adj;
};

void BFS(grafo G, int s, int tamanho)    //Busca em Largura(Breadth First Search)
{
    char color[tamanho];  //w = white; g = gray; b = black
    int d[tamanho];       //-1 = infinito
    int pi[tamanho];      //-1 = null
    fila Q;
    int u;

    for (u = 0; u<tamanho; u++)
    {
        if(u!=s)
        {
            color[u] = 'w';
            d[u] = -1;
            pi[u] = -1;
        }
    }
    color[s] = 'g';
    d[s] = 0;
    InsereFila(Q,s);
    while (!FilaVazia(Q))
    {
        u = BuscaInicio(Q)->chave;
        for (noLSE* v = G.Adj[u].primeiro; v != NULL; v=v->prox)
        {
            if (color[v->chave]='w')
            {
                color[v->chave]='g';
                d[v->chave]=d[u]+1;
                pi[v->chave]=u;
                InsereFila(Q,v->chave);
            } 
        }
        RemoveFila(Q);
        color[u]='b';
    }

    cout<<"d: ";
    for (size_t i = 0; i < tamanho; i++)
    {
        cout<<d[i]<<" ";
    }
    cout<<endl<<"pi:";
    for (size_t i = 0; i < tamanho; i++)
    {
        cout<<pi[i]<<" ";
    }
    cout<<endl<<"c: ";
    for (size_t i = 0; i < tamanho; i++)
    {
        cout<<color[i]<<" ";
    }    
}

int main()
{
    grafo grafom;
    int tam = 6;
    grafom.Adj = new LSE[tam];
    
    InsereFimLSE(grafom.Adj[0],1);
    InsereFimLSE(grafom.Adj[0],3);
    InsereFimLSE(grafom.Adj[1],0);
    InsereFimLSE(grafom.Adj[1],2);
    InsereFimLSE(grafom.Adj[2],1);
    InsereFimLSE(grafom.Adj[3],0);
    InsereFimLSE(grafom.Adj[3],4);
    InsereFimLSE(grafom.Adj[3],5);
    InsereFimLSE(grafom.Adj[4],3);
    InsereFimLSE(grafom.Adj[4],5);
    InsereFimLSE(grafom.Adj[5],3);
    InsereFimLSE(grafom.Adj[5],4);
    BFS(grafom,0,tam);
    return 0;
}