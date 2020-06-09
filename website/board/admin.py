from django.contrib import admin
from board.models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # models.py에서 tags는 TaggableManager 클래스로 정의하였으므로
    # list_display에 업데이트하기 위해, tag_list 항목을 메소드로 정의
    list_display = ('id', 'title', 'modify_dt', 'tag_list')
    list_filter = ('modify_dt',)
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}

#tag 관련 함수 추가
    #Post 레코드 리스트를 가져오는 메소드 오버라이딩
    #Tag 테이블의 관련 레코드를 한 번의 쿼리로 미리 가져옴
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    #tag_list에 보여줄 항목
    #name 필드의 값들을 ,로 연결하여 보여줌
    def tag_list(self, obj):
        return ', '.join(o.name for o in obj.tags.all())