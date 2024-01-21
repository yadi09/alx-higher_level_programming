#include "lists.h"



/**
 * reverse_nodes - function
 * @head: singly linked list
 * Return: void
 **/

void reverse_nodes(listint_t **head)
  {
    listint_t *prev = NULL;
    listint_t *current = *head;
    listint_t *next = NULL;

    while (current != NULL)
      {
	next = current->next;
	current->next = prev;
	prev = current;
	current = next;
      }

    *head = prev;
  }


/**
 * is_palindrom - function
 * @head: singly linked list
 * Return: 0 or 1
 **/

int is_palindrome(listint_t **head)
{
  listint_t *first = *head;
  listint_t *last = *head;
  listint_t *prev = NULL;

  if (!head || !*head || !(*head)->next)
    return (1);

   while (last != NULL && last->next != NULL)
    {
        last = last->next->next;
        prev = first;
        first = first->next;
    }

    if (last != NULL)
    {
        first = first->next;
    }

    prev->next = NULL;
    reverse_nodes(&first);

    while (*head != NULL && first != NULL)
    {
      if ((*head)->n != first->n)
            return 0;
      (*head) = (*head)->next;
      first = first->next;
    }

    if (*head == NULL && first == NULL)
        return 1;
    else
        return 0;
    

  return (1);
}
