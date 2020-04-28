#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle - check if there is a cycle in the linked list
 * @list: pointer to the list
 * Return: 1 if there is a cycle otherwise 0
 */
int check_cycle(listint_t *list)
{
	listint_t *one_step = list, *two_step = list;

	while (two_step != NULL && two_step->next != NULL)
	{
		one_step = one_step->next;
		two_step = two_step->next;
		two_step = two_step->next;
		if (one_step == two_step)
			return (1);
	}
	return (0);
}
