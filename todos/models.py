from django.db import models

# Model represents the "Todo" table in the Postgres database.
# Each field below becomes a column in that table.
class Todo(models.Model):
    # Short text field for the todo's title, max 200 characters
    title = models.CharField(max_length=200)

    # Optional longer text field for extra details; blank=True means
    # it's not required when submitting a form
    description = models.TextField(blank=True)

    # Boolean flag to track whether the task is done, defaults to False
    completed = models.BooleanField(default=False)

    # Automatically set to the current timestamp when the row is first created
    created_at = models.DateTimeField(auto_now_add=True)

    # Automatically updated to the current timestamp every time the row is saved
    updated_at = models.DateTimeField(auto_now=True)

    # Controls default ordering when querying Todos (newest first)
    class Meta:
        ordering = ['-created_at']

    # Defines how a Todo object is displayed as a string (e.g. in Django admin)
    def __str__(self):
        return self.title
