#pragma once
#include "stdafx.h"

/*
----------------------------
LISTA SIMPLESMENTE ENCADEADA
----------------------------
*/

using namespace std;

struct noLSE//NÓ DA LISTA SIMPLESMENTE ENCADEADA
{
	int chave;
	noLSE *prox;
};

struct LSE//LISTA SIMPLESMENTE ENCADEADA
{
	noLSE *primeiro;
	noLSE *ultimo;
};


void InicializaLSE(LSE &L)
{
	L.primeiro = NULL;
	L.ultimo = L.primeiro;
}

bool VaziaLSE(LSE L)
{
	return(L.primeiro == NULL && L.ultimo == NULL);
}

noLSE *BuscaLSE(LSE L, int x)
{
	noLSE *no;
	no = L.primeiro;
	while (no != NULL && no->chave != x)
	{
		no = no->prox;
	}
	return(no);
}

void InsereInicioLSE(LSE &L, int x)
{
	noLSE *no;
	no = new noLSE;
	if (no == NULL)
	{
		cout << "OVERFLOW"<<endl;
	}
	else
	{
		no->chave = x;
		no->prox = L.primeiro;
		L.primeiro = no;
		if (VaziaLSE(L))
		{
			L.ultimo = no;
		}
	}
}

void InsereFimLSE(LSE &L, int x)
{
	noLSE *no;
	no = new noLSE;
	if (no == NULL)
	{
		cout << "OVERFLOW"<<endl;
	}
	else
	{
		no->chave = x;
		no->prox = NULL;
		if (!VaziaLSE(L))
		{
			L.ultimo->prox = no;
		}
		else
		{
			L.primeiro = no;
		}
		L.ultimo = no;
	}
}

void InsereOrdenadoLSE(LSE &L, int x)
{
	if (VaziaLSE(L) || x <= L.primeiro->chave)
	{
		InsereInicioLSE(L, x);
	}
	else if (x >= L.ultimo->chave)
	{
		InsereFimLSE(L, x);
	}
	else
	{
		noLSE *no, *aux;
		no = new noLSE;
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

			no->prox = aux->prox;
			aux->prox = no;
		}
	}
}

noLSE *RemoveLSE(LSE &L, int x)
{
	if (VaziaLSE(L))
	{
		cout << "UNDERFLOW" << endl;
		return NULL;
	}
	else
	{
		noLSE *ret;
		ret = NULL;

		if (L.primeiro->chave == x)
		{
			if (L.primeiro == L.ultimo)
			{
				ret = L.primeiro;
				L.primeiro = NULL;
				L.ultimo = NULL;
			}
			else
			{
				ret = L.primeiro;
				L.primeiro = L.primeiro->prox;
			}
		}
		else
		{
			noLSE *aux;
			aux = L.primeiro;

			while (aux->prox == NULL && aux->prox->chave != x)
			{
				aux = aux->prox;
			}

			if (aux->prox == NULL)
			{
				cout << "Elemento nao encontrado"<<endl;
				return ret;
			}
			else
			{
				ret = aux->prox;
				aux->prox = ret->prox;
				ret->prox = NULL;

				if (ret = L.ultimo)
				{
					L.ultimo = aux;
				}
			}
		}
		return(ret);
	}
}