#include "lists.h"

/**
 * is_palindrom - function
 * @head: singly linked list
 * Return: 0 or 1
 **/

int is_palindrome(listint_t **head)
{
  listint_t *first_node = *head;
  listint_t *last_node = *head;
  listint_t *length_node = *head;
  int len = 0, i, j;
  int l_len = 0;

  if (!head || !*head)
    return (1);

  while (length_node->next)
    {
      length_node = length_node->next;
      len++;
    }

  for (i = 0; i < (l_len / 2); i++)
    {
      len = len - 1;
      while (j < len)
	{
	  last_node = last_node->next;
	  j++;
	}
      if (first_node->n != last_node->n)
	{
	  return (0);
	}
      first_node = first_node->next;
    }

  return (1);
}
