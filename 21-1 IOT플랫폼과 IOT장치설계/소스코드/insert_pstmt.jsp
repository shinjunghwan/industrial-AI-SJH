<%@page import= "java.sql.Statement"%>
<%@page import= "java.sql.PreparedStatement"%>
<%@page import= "java.sql.Connection"%>
<%@page import= "java.sql.DriverManager"%> <%@
<%page language= "java" contentType= "text/html; charset=UTF-8" pageEncoding= "UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv= "Content-Type" content= "text/html; charset=UTF-8">
<title>Insert title here</title>
</head>
<body>
<%
 String driverName= "org.mariadb.jdbc.Driver";
String url = "jdbc:mysql://localhost:3306/sjh_db";
String id = "root";
 String pwd = "jung571109914";

 request.setCharacterEncoding( "utf-8" );
String code = request.getParameter( "code" );
String irum = request.getParameter( "irum" );
String celphone = request.getParameter( "celphone" );

 Class.forName(driverName );
Connection conn = DriverManager.getConnection(url,id,pwd );
//PreparedStatement객체를 통한 쿼리 작업
String preSql = "insert info values(?,?,?)";
PreparedStatement pstmt = conn.prepareStatement(preSql );
 pstmt.setString( 1, code );
pstmt.setString( 2, irum );
pstmt.setString( 3, celphone );
 int r = pstmt.executeUpdate( );

  if (r== 1 ) {
out.println( "1개 데이터 추가 성공" );
 }

  pstmt.close( );
conn.close( );
%>
</body>
</html>