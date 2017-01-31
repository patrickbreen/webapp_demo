from django.contrib.auth.models import User
from django.utils import timezone

from app_forum.models import Category, Thread, Comment

u = User()
u.save()

c = Category(name="general discussion")
c.save()

t = Thread(text="lets talk about something in this new thread",
        title="new interesting thread",
        modified=timezone.now(),
        is_message_thread=False,
        created_by=u,
        category=c
        )

t.save()

c = Comment(likes=0,
        text="here is the first comment",
        has_been_read=False,
        message_comment=False,
        created=timezone.now(),
        created_by=u,
        # no recipients
        thread=t
        )
c.save()


# make superuser
User.objects.create_superuser('admin', '', 'asldfhbli')
