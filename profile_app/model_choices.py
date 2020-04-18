ACT_CREATE, ACT_EDIT, ACT_DELETE = range(1, 4)
ACTION_CHOICES = (
    (ACT_CREATE, 'Create'),
    (ACT_EDIT, 'Edit'),
    (ACT_DELETE, 'Delete'),
)

AcTION_CHOICES_DICT = {i[0]: i[1] for i in ACTION_CHOICES}
