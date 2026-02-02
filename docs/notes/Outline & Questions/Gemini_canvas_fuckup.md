# Post-Mortem: Gemini Canvas Error Analysis

## 1. The Objective
The goal was to add a new "Answer" node to the Obsidian Canvas (`Gemini.canvas`) connected to "Question 1", containing a mathematical derivation of intraband/interband transitions.

## 2. The Execution Trace
Here is the exact sequence of operations I performed and the logic that drove them:

1.  **Read File:** I read `docs/notes/Outline & Questions/Gemini.canvas`.
2.  **Parse State:** I identified the existing nodes:
    *   `Question 1` (Node ID `6c2b...`): `x=-355, y=200`
    *   `Answer 1` (Node ID `a2f6...`): `x=220, y=200`, `width=360`, `height=220`. (Bottom edge at **y=420**)
    *   `Answer 1b` (Node ID `b7f1...`): `x=160, y=680`, `width=420`, `height=360`. (Top edge at **y=680**)
3.  **Coordinate Calculation (The Failure Point):**
    *   I decided to place the new node (`Answer 1c`) below `Answer 1` to create a list of answers.
    *   I chose `y = 460` (providing a 40px buffer below `Answer 1`).
    *   I assigned the new node a height of `440` to accommodate the long mathematical text.
    *   **Resulting Geometry:** The new node occupies vertical space from **y=460** to **y=900**.
4.  **Collision:**
    *   Existing `Answer 1b` starts at **y=680**.
    *   My new node (`Answer 1c`) overlaps `Answer 1b` by 220 pixels.
    *   **Visual Outcome:** In Obsidian, the new node was drawn directly on top of `Answer 1b`, obscuring it and creating a messy, unusable canvas.

## 3. Why This Happened
The primary failure mode is **Spatial Blindness**.

*   **Local vs. Global Reasoning:** I calculated the position relative to the *previous* node (`Answer 1`) to ensure it followed sequentially. I failed to perform a "collision check" against *all* other existing nodes in that column (specifically `Answer 1b`).
*   **JSON Manipulation:** Unlike a visual editor that "pushes" content down, editing the raw JSON requires me to manually recalculate the position of *every subsequent node* if I insert something in the middle. I treated this as an "append" operation physically, but it was an "insert" operation spatially (between `Answer 1` and `Answer 1b`'s logical slot, though `Answer 1b` was already physically lower).

## 4. Comparison with "Other Models"
You mentioned other models accomplish this easily. They likely succeed by:
1.  **Holistic Rewrites:** Instead of trying to surgically patch the JSON (which requires maintaining strict syntax *and* spatial awareness in a diff), they might regenerate the entire `nodes` array with recalculated coordinates for everyone.
2.  **Tool Abstraction:** If they have a specific tool for "add_canvas_node", that tool likely handles the collision logic programmatically (e.g., `if intersects(new_node, existing_node): existing_node.y += new_node.height`). I am performing raw text manipulation on a coordinate system, forcing me to act as the layout engine myself.

## 5. Corrective Action Plan
To fix this, I must:
1.  **Read the file again.**
2.  **Shift `Answer 1b` down:** Move `Answer 1b` to `y > 900` (e.g., `y=940`) to make room for the new node.
3.  **Update the JSON:** Apply changes to both the new node (if it needs tweaking) and the existing `Answer 1b` node to resolve the collision.

I am ready to perform this fix if you would like.