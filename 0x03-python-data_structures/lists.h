#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>
#include <stdio.h>

/**
 * struct listint_s - singly linked list
 * @n: int
 * @next: nxt node
 *
 * linked list
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
void free_listint(listint_t *head);
listint_t *add_nodeint_end(listint_t **head, const int n);
int is_palindrome(listint_t **head);

#endif

