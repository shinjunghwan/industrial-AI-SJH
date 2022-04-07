<%@page import="java.sql.SQLException"%>
<%@page import="java.sql.PreparedStatement"%>
<%@page language="java" contentType="text/html; charset=EUC-KR" pageEncoding="EUC-KR"%>
<%@page import="java.sql.Connection"%>
<%@page import="util.dbhelper.DBconn"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/lose.dtd>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Insert title here</title>
</head>
<body>
<%
request.setCharacterEncoding("utf-8");
String id = request.getParameter("id");
String pwd = request.getParameter("pwd");
String email = request.getParameter("email");
String phone = request.getParameter("phone");
String any = "2020/12/13";
Connection con = null;
PreparedStatement pstmt = null;
String sql = "insert members values(?,?,?,?,?)";
int n = 0;
try {
con = DBconn.getConnection();
pstmt = con.prepareStatement(sql);
pstmt.setString(1, id);
pstmt.setString(2, pwd);
pstmt.setString(3, email);
pstmt.setString(4, phone);
pstmt.setString(5, any);
//pstmt.setString(5, null);
n = pstmt.executeUpdate();
} catch(SQLException se) {
System.out.println(se.getMessage());
} finally {
try {
if(pstmt != null) pstmt.close();
if(con != null) con.close();
} catch(SQLException se) {
System.out.println(se.getMessage());
}
}
%>
<script type="text/javascript">
if(<%=n%> > 0) {
alert("success isnert.");
 location.href="../sjhindex.html";
} else {
alert("fail insert.");
location.href="../sjhindex.html"
}
</script>
</body>
</html>