import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.annotation.*;

@WebServlet("http://ip_addr:port/hello/sayhello")
public class HelloServlet extends HttpServlet {

	// The doGet() runs once per HTTP GET request to this servlet.
	@Override
	public void doGet(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {
			response.setContentType("text/html");

			PrintWriter out = response.getWriter();

			out.println("<!DOCTYPE html>");
			out.println("<html>");
			out.println("<head><title>Hello World</title></head>");
			out.println("<body>");
			out.println("<h1>Hello, World</h1>");
			out.println("<p>Request URI: " + request.getRequestRUI() + "</p>" );
			out.println("<p>Protocol: " + request.getProtocol() +"</p>");
			out.println("<p>PathInfor: "+ request.PathInfo() + "</p>");
			out.println("<p>Remotasdasde Address: " + request.getRemoteAddr()+"</p>");
			out.println("<p>A Random Number: <strong>" + Math.random() + "</strong></p>");
			out.println("</body></html>");
			out.close();

		}

}
