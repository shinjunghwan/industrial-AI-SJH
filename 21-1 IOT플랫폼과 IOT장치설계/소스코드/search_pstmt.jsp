<%@page import="java.sql.PreparedStatement"%>
<%@page import="util.dbhelper.DBconn"%>
<%@page import="java.sql.ResultSet"%>
<%@page import="java.sql.Connection"%>
<%@ page language= "java" contentType= "text/html; charset=UTF-8" pageEncoding= "UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv= "Content-Type" content= "text/html; charset=UTF-8">
<title>Insert title here</title>
</head>
<body>
<%
String code=request.getParameter( "code" );
//out.println("code=>"+code);
Connection conn = DBconn.getConnection( ); //Connection 객체 얻기.
String sql = "Select * from info where code=?";
PreparedStatement pstmt = conn.prepareStatement(sql );
pstmt.setString( 1, code );
ResultSet rs = pstmt.executeQuery( );
//실행 -> 조회

if(rs.next( ) ) { //검색된 결과가 존재하면 true
String r_code = rs.getString( "code" ); //columnIndex or columnLabel
String r_irum = rs.getString( "irum" ); //columnIndex or columnLabel
//String r_celphone = rs.getString(3);
//columnIndex or //columnLabel
String r_celphone = rs.getString( "celphone" );
%>
<h1>조회결과</h1> <table border= "1">
<tr>
 <td>코드</td>
<td><%=r_code %></td>
</tr>
<tr>
<td>품명</td>
<td><%=r_irum %></td>
</tr>
<tr>
<td>담당연락처</td>
<td><%=r_celphone %></td>
</tr>
</table>


<%
} else {
out.println( "입력하신 "+code+ "는 존재하지 않습니다." );
}

rs.close( );
pstmt.close( );
DBconn.close( );

%>
</body>
</html>
