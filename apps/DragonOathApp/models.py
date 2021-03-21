from django.db import models

# Create your models here.

class Mark(models.Model):
    mark = models.CharField(max_length=2, verbose_name='字母')

    class Meta:
        db_table = 'django_mark'
        verbose_name = '字母'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.mark

class ForeignAuthor(models.Model):
    author = models.CharField(max_length=32, verbose_name='作者')
    brief = models.TextField(verbose_name='简介')
    mark = models.ForeignKey(Mark, on_delete=models.CASCADE, verbose_name='字母')

    def __str__(self):
        return self.author

class BooksInfo(models.Model):
    book_name = models.CharField(max_length=32, verbose_name="书名")
    content = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'django_books'
        verbose_name = '书籍'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.book_name

class Userinfo(models.Model):
    user_name = models.CharField(max_length=10, verbose_name='账号')
    passwd = models.CharField(max_length=32, verbose_name='密码')
    gmail = models.EmailField(null=False, unique=True)

    # roles = models.ForeignKey('RoleInfo', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'django_users'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user_name

class Author(models.Model):
    author_name = models.CharField(max_length=10, verbose_name='作家')
    brief = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'django_author'
        verbose_name = '作者'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.author_name


class Pageview(models.Model):
    read = models.IntegerField(verbose_name='阅读量', blank=True, null=True)
    comments = models.IntegerField(verbose_name='评论数', blank=True, null=True)
    book = models.ForeignKey(BooksInfo, on_delete=models.CASCADE, verbose_name='书籍', blank=True, null=True)

    class Meta:
        db_table = 'django_pageview'
        verbose_name = '阅读量'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.read

class Roleinfo(models.Model):
    definition = (
        ("dps", "DPS"),
        ("tank", "TANK"),
        ("healer", "healer")
    )
    gender = (
        ("gentleman", "gentleman"),
        ("madam", "madam")
    )
    role_class = models.CharField(choices=definition, default="dps", verbose_name="职业", max_length=10)
    role_gender = models.CharField(choices=gender, default="gentleman", verbose_name="性别", max_length=10)
    role_name = models.CharField(max_length=10, verbose_name="角色名")
    role_user = models.ForeignKey(Userinfo, on_delete=models.CASCADE, verbose_name='用户')

    class Meta:
        db_table = 'django_roles'
        verbose_name = '角色'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.role_name

class Holmes(models.Model):
    book_name = models.CharField(max_length=32, verbose_name='书名')
    content = models.TextField(verbose_name='内容')
    book = models.ForeignKey(BooksInfo, on_delete=models.CASCADE, verbose_name='书籍ID')

    class Meta:
        db_table = 'django_holmes'
        verbose_name = '福尔摩斯'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.book_name
