import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

class TreeNode {
    String name;
    List<TreeNode> children;

    public TreeNode(String name) {
        this.name = name;
        this.children = new ArrayList<>();
    }

    public void addChild(TreeNode child) {
        this.children.add(child);
    }
}

public class Part3Tree {

    public static void printTreeStructure() {
        String treeStr = """
         [ Subjects ]
          /        \\
     [Math]        [Science]
     /    \\         /     \\
[Algebra] [Geometry] [Physics] [Chemistry]
""";
        System.out.println(treeStr);
    }

    public static void levelOrderTraversal(List<TreeNode> roots) {
        Queue<TreeNode> queue = new LinkedList<>(roots);
        List<String> traversalOrder = new ArrayList<>();

        System.out.println("--- Dry Run: Level Order Traversal ---");
        int level = 0;
        while (!queue.isEmpty()) {
            int levelSize = queue.size();
            List<String> levelNodes = new ArrayList<>();
            for (int i = 0; i < levelSize; i++) {
                TreeNode node = queue.poll();
                levelNodes.add(node.name);
                traversalOrder.add(node.name);
                for (TreeNode child : node.children) {
                    queue.add(child);
                }
            }
            System.out.println("Level " + level + ": " + String.join(", ", levelNodes));
            level++;
        }

        System.out.println("\nLevel Order Traversal Visit Order: " + String.join(", ", traversalOrder));
    }

    public static void main(String[] args) {
        TreeNode math = new TreeNode("Math");
        math.addChild(new TreeNode("Algebra"));
        math.addChild(new TreeNode("Geometry"));

        TreeNode science = new TreeNode("Science");
        science.addChild(new TreeNode("Physics"));
        science.addChild(new TreeNode("Chemistry"));

        List<TreeNode> topLevels = List.of(math, science);

        System.out.println("--- Tree Visualization ---");
        printTreeStructure();

        levelOrderTraversal(topLevels);
    }
}
