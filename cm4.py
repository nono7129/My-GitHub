Public Sub GeneratePassword()
    Dim passwordLength As Integer
    Dim password As String
    Dim charset As String
    charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_=+"

    ' 비밀번호 길이 입력 받기
    passwordLength = Val(InputBox("비밀번호 길이를 입력하세요:"))

    ' 입력값이 숫자가 아닌 경우 오류 처리
    If Not IsNumeric(passwordLength) Then
        MsgBox "숫자를 입력하세요."
        Exit Sub
    End If

    ' 비밀번호 생성
    password = ""
    For i = 1 To passwordLength
        password = password & Mid(charset, Int((Len(charset) * Rnd) + 1), 1)
    Next i

    ' 생성된 비밀번호 출력
    MsgBox "안전한 비밀번호: " & password
End Sub

