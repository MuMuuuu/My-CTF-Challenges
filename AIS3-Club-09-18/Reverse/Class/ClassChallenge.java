import java.util.Scanner;

public class ClassChallenge {
	public static void main(String[] args){
		ClassChallenge task = new ClassChallenge();
		System.out.println("Please tupni the tcerroc password");
		Scanner inp = new Scanner(System.in);
		if(task.check(inp.next().strip())){
		    System.out.println("Correct emocleW");
		}
		else{
		    System.out.println("Dont yrt to kcah me");
		}
	}
	public boolean check(String pass){
		return pass.substring(22,26).equals("3_ch") && 
			   pass.substring(24,27).equals("ch4") && 
			   pass.substring(1,3).equals("IS") && 
			   pass.substring(7,11).equals("_w0w") && 
			   pass.substring(8,11).equals("w0w") && 
			   pass.substring(38,41).equals("Ez_") && 
			   pass.substring(14,19).equals("3ms_t") && 
			   pass.substring(33,37).equals("_t0O") && 
			   pass.substring(45,49).equals("YoU}") && 
			   pass.substring(30,34).equals("_15_") && 
			   pass.substring(13,17).equals("e3ms") && 
			   pass.substring(15,17).equals("ms") && 
			   pass.substring(12,17).equals("se3ms") && 
			   pass.substring(24,29).equals("ch4l1") && 
			   pass.substring(41,44).equals("f0r") && 
			   pass.substring(2,6).equals("S3{0") && 
			   pass.substring(5,10).equals("0h_w0") && 
			   pass.substring(15,18).equals("ms_") && 
			   pass.substring(23,26).equals("_ch") && 
			   pass.substring(10,15).equals("w_se3") && 
			   pass.substring(4,6).equals("{0") && 
			   pass.substring(47,49).equals("U}") && 
			   pass.substring(41,45).equals("f0r_") && 
			   pass.substring(24,29).equals("ch4l1") && 
			   pass.substring(34,38).equals("t0O_") && 
			   pass.substring(41,43).equals("f0") && 
			   pass.substring(30,35).equals("_15_t") && 
			   pass.substring(27,30).equals("l1s") && 
			   pass.substring(11,16).equals("_se3m") && 
			   pass.substring(8,13).equals("w0w_s") && 
			   pass.substring(0,4).equals("AIS3") && 
			   pass.substring(0,5).equals("AIS3{") && 
			   pass.substring(42,46).equals("0r_Y") && 
			   pass.substring(35,39).equals("0O_E") && 
			   pass.substring(17,22).equals("_theS") && 
			   pass.substring(9,12).equals("0w_") && 
			   pass.substring(21,23).equals("S3");
	}
}

