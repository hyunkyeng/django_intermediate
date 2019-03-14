from django.db import models

# Create your models here.
class Board(models.Model):
    # id primary key 는 기본적으로 처음 테이블 생성시 자동으로 만들어진다.
    # id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    
class Comment(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.content
        
    # on_delete : 참조하는 부모객체가 사라졌을 때, 부모에 딸려있는 자식 객체들을 어떻게 처리할지 정의한다.
    
    # 데이터베이스 무결성
    # 1. 개체 무결성 : PK/ NOT NULL/ UNIQUE
    #   - 식별자는 NULL 일 수 없고 중복일 수 없다.
    # 2. 참조 무결성 : FK/ 모든 외래 키의 값은 2가지 상태 가운데 하나에만 속함을 규정
    # 3. 범위/ 도메인 무결성 : 컬럼은 지정된 형식을 반드시 만족해야 된다. (CHAR, TEXT)
    
    # on_delete 속성 값
    # 1. CASCADE : 부모객체가 삭제 됐을 때 이를 참조하는 객체도 삭제한다.
    # 2. PROTECT : 참조가 되어있는 경우 삭제 오류 발생.
    # 위 2개가 가장 많이 쓰인다.
    # 3. SET_NULL : 부모객체가 삭제 됐을 때 참조하는 모든 값을 NULL로 치환(NOT NULL 조건시 불가능)
    # 4. SET_DEFAULT : 모든 값이 DEFAULT 로 치환.
    # 5. SET() : 특정 함수 호출.
    # 6. DO_NOTHING : 아무것도 하지 않음. 다만, SQL에서는 on_delete 직접 설정해줘야함.