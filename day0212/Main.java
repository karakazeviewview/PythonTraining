import java.util.*;
public class Main{
	public static void main(String[] args){
		Scanner sc=new Scanner(System.in);
		Random rand=new Random();
		String[] fortunes=new String[10000];
		for(int i=0;i<fortunes.length;i++){
			fortunes[i]=String.format("%04d",i);
		}
		//System.out.println(Arrays.toString(fortunes));
		for(int i=0;i<fortunes.length-1;i++){
			int index=rand.nextInt(fortunes.length-i);
			String temp=fortunes[index];
			fortunes[index]=fortunes[fortunes.length-1-i];
			fortunes[fortunes.length-1-i]=temp;
		}
		System.out.print("何枚くじを買いますか?>>");
		int num=sc.nextInt();
		String[] myLotts=new String[num];
		for(int i=0;i<num;i++){
			myLotts[i]=fortunes[i];
		}
		Arrays.sort(myLotts);
		System.out.println(Arrays.toString(myLotts));
		System.out.println("抽選開始...");
		String lucky=String.format("%04d",rand.nextInt(10000));
		for(int i=0;i<4;i++){
			Thread.sleep(1000);
			System.out.println(lucky.charAt(i));
		}
	}
}
