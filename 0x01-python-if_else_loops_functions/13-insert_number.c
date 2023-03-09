#include "lists.h"

/**
*insert_node - inserts a new node
*@head: first parameter
*@number: second parameter
*Return: address at success, NULL at failure.
*/
listint_t *insert_node(listint_t **head, int number)
{
listint_t *new;
listint_t *ptr;
listint_t *ptr_prev;

ptr = *head;
new = malloc(sizeof(listint_t));

if (new == NULL)
return (NULL);

while (ptr != NULL)
{
if (ptr->n > number)
break;
ptr_prev = ptr;
ptr = ptr->next;
}

new->n = number;

if (*head == NULL)
{
new->next = NULL;
*head = new;
}
else
{
new->next = ptr;
if (ptr == *head)
*head = new;
else
ptr_prev->next = new;
}

return (new);
}
