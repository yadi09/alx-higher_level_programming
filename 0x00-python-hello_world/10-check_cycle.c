#include "lists.h"
#include <stdio.h>

int check_cycle(listint_t *list) {
  listint_t *temp = list;
  listint_t *temp2 = list;

  while (temp2 != NULL && temp2->next != NULL) {
    temp = temp->next;
    temp2 = temp2->next->next;

    if (temp == temp2) {
      return 1;
    }
  }

  return 0;
}
