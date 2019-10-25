#pragma once
#include "stdafx.h"

/*
--------------------------
LISTA DUPLAMENTE ENCADEADA
--------------------------
*/

using namespace std;

struct noLDE
{
	int chave;
	noLDE *ant;
	noLDE *prox;
};

struct LDE
{
	noLDE *primeiro, *ultimo;
};

void InicializaLDE(LDE &L)
{
	L.primeiro = NULL;
	L.ultimo = NULL;
}

bool VaziaLDE(LDE L)
{
	return(L.ultimo == NULL);
}

noLDE *BuscaLDE(LDE L, int x)
{
	noLDE *no;
	no = L.primeiro;
	while (no != NULL && no->chave != x)
	{
		no = no->prox;
	}
	return(no);
}

void InsereInicioLDE(LDE &L, int x)
{
	noLDE *no = new noLDE;
	if (no == NULL)
	{
		cout << "OVERFLOW"<<endl;
	}
	else
	{
		no->chave = x;
		no->ant = NULL;
		no->prox = NULL;
		if (VaziaLDE(L))
		{
			L.ultimo = no;
		}
		else
		{
			L.primeiro->ant = no;
		}
		L.primeiro = no;
	}
}

void InsereFimLDE(LDE &L, int x)
{
	noLDE *no = new noLDE;
	if (no == NULL)
	{
		cout << "OVERFLOW"<<endl;
	}
	else
	{
		no->chave = x;
		no->prox = NULL;
		no->ant = L.ultimo;
		
		if (VaziaLDE(L))
		{
			L.primeiro = no;
		}
		else
		{
			L.ultimo->prox = no;
		}
		L.ultimo = no;
	}
}

void InsereOrdenadoLDE(LDE &L, int x)
{
	if (VaziaLDE(L) || x <= L.primeiro->chave)
	{
		InsereInicioLDE(L, x);
	}
	else if (x >= L.ultimo->chave)
	{
		InsereFimLDE(L, x);
	}
	else 
	{
		noLDE *no, *aux;
		no = new noLDE;
		if (no == NULL)
		{
			cout << "OVERFLOW"<<endl;
		}
		else
		{
			no->chave = x;
			aux = L.primeiro;
			while (aux->prox->chave < x)
			{
				aux = aux->prox;
			}
			no->ant = aux;
			no->prox = aux->prox;
			no->prox->ant = no;
			aux->prox = no;
		}
	}
}

noLDE *RemoveLDE(LDE &L, int x)
{
	noLDE *no;
	no = BuscaLDE(L, x);
	if (no == NULL)
	{
		cout << "Elemento não encontrado" << endl;
	}
	else
	{
		if (L.primeiro == L.ultimo)
		{
			no = L.primeiro;
			InicializaLDE(L);
		}
		else if (L.primeiro == no)
		{
			L.primeiro = no->prox;
			L.primeiro->ant = NULL;
			no->prox = NULL;
		}
		else if (L.ultimo == no)
		{
			L.ultimo = no->ant;
			L.ultimo->prox = NULL;
			no->ant = NULL;
		}
		else
		{
			no->ant->prox = no->prox;
			no->prox->ant = no->ant;
			no->prox = NULL;
			no->ant = NULL;
		}
	}
	return(no);
}