#pragma once
#include"LDE.h"
#include"stdafx.h"

/*
----
FILA
----
*/

using namespace std;

struct fila
{
	noLDE *primeiro, *ultimo;
};

void InicializaFila(fila &Q)
{
	Q.primeiro = NULL;
	Q.ultimo = NULL;
}

bool FilaVazia(fila Q)
{
	return(Q.primeiro == NULL && Q.ultimo == NULL);
}

bool FilaCheia()
{
	noLDE *no = new noLDE;
	return(no == NULL);
}

void InsereFila(fila &Q, int x)
{
	if (!FilaCheia())
	{
		noLDE *no = new noLDE;
		no->chave = x;
		no->prox = NULL;

		if (FilaVazia(Q))
		{
			no->ant = NULL;
			Q.primeiro = no;
			Q.ultimo = no;
		}
		else
		{
			no->ant = Q.ultimo;
			Q.ultimo->prox = no;
			Q.ultimo = no;
		}
	}
	else
	{
		cout << "OVERFLOW"<<endl;
	}
}

noLDE *RemoveFila(fila &Q)
{
	noLDE *ret = NULL;
	if (FilaVazia(Q))
	{
		cout << "UNDERFLOW" << endl;
	}
	else if(Q.primeiro==Q.ultimo)
	{
		ret = Q.ultimo;
		InicializaFila(Q);
	}
	else
	{
		ret = Q.primeiro;
		Q.primeiro = Q.primeiro->prox;
		Q.primeiro->ant = NULL;
	}
	return(ret);
}

noLDE *BuscaInicio(fila Q)
{
	return(Q.primeiro);
}