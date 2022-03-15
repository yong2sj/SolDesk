package classtest;

/*
	변수의 scope
		▶ 클래스 변수
		▶ 인스턴스 변수(멤버변수)
			==> 선언위치 : 클래스 영역
			==> 생성시기
				- 클래스변수 : 클래스가 메모리에 올라갈 떄
				- 인스턴스변수 : 인스턴스(객체)가 생성되었을 때
		▶ 로컬 변수(지역변수) 
			==> 선언위치 : 메소드, 생성자 내부, 블록문 내부 ...
			==> 생성시기 : 변수 선언문이 수행될 때
*/

public class Variables {
	int num; // 인스턴스 변수
	static int cv; // 클래스 변수
	
	void method() {
		int lv = 0; // 로컬변수
	}
}