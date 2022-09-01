from notes.models import Notes
import factory

# todo:In Progress (Due to some errors)


class NotesFactory(factory.DjangoModelFactory):
    class Meta:
        model = "Notes"
        django_get_or_create = (
            "title",
            "text",
            "date_created",
            "date_updated",
            "user",
            "archive",
            "sharedwith",
        )
