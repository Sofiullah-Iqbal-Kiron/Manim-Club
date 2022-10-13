import java.io.BufferedReader;
import java.io.InputStreamReader;

class runner {
    public static void main(String[] args) {
        try {
            Process p = Runtime.getRuntime().exec("manim -pql Main.py Shape");
            StringBuilder output = new StringBuilder();
            BufferedReader reader = new BufferedReader(new InputStreamReader(p.getInputStream()));
            String line;
            while ((line = reader.readLine()) != null) {
                output.append(line + '\n');
            }
            if (p.waitFor() == 0)
                System.out.println(output);
            System.out.println(p.getOutputStream().toString());
        } catch (Exception e) {
            System.out.println("Error");
        }
    }
}