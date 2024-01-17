#include "lists.h"
#include <stdio.h>

/**
 *
 **/

int check_cycle(listint_t *list){
  listint_t *temp = list;
  listint_t *node;
  listint_t *temp_temp;

  while (temp != NULL)
    {
      node = temp;
      temp_temp = temp;

      while (temp != NULL)
	{
	  if (node == temp->next)
	    {
	      return (1);
	    }
	  temp = temp->next;
	}
      temp = temp_temp->next;
    }

  return (0);
}
