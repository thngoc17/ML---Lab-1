### Scene 4: Phước lành của cấu trúc chiều thấp (3:35 - 4:45)
**Mục tiêu:** Đưa ra giả định MoLRG để giải quyết Curse of Dimensionality.

* **[3:35 - 3:55] Manim Visual:** Dùng `ThreeDAxes` xoay một không gian 3D rộng lớn. Rải vài `Dot3D` lơ lửng, cách xa nhau. Hiện chữ "Curse of Dimensionality".
* **[3:55 - 4:20] Manim Visual:** Camera xoay góc. Bất ngờ hiện ra một `ParametricSurface` 2D mỏng manh đi qua tất cả các điểm đó. Các điểm này thực chất nằm trọn trên mặt phẳng này. Hiện chữ "Intrinsic Dimension $r \ll d$".
* **[4:20 - 4:45] Manim Visual:** Dùng `MathTex` hiện công thức phân phối hỗn hợp Gauss hạng thấp:
    $$p_{data}(x) = \frac{1}{K} \sum_{i=1}^K \mathcal{N}(x; 0, U_i U_i^T)$$
    Vẽ các hệ vector cơ sở $U_1, U_2$ ngay trên mặt phẳng để minh họa không gian con.

**[Voiceover]**
"Nếu dữ liệu lấp đầy mọi ngóc ngách của không gian vật lý, ta sẽ cần một lượng mẫu khổng lồ, tăng theo hàm mũ của số chiều. 
May mắn thay, dữ liệu thực tế mang đến một 'phước lành'. Một bức ảnh không phải là tập hợp pixel ngẫu nhiên, chúng bị ràng buộc bởi hình khối và ánh sáng. Toàn bộ kho tàng hình ảnh tự nhiên, trên thực tế, lại cư ngụ trên những không gian con có số chiều nội tại cực kỳ nhỏ.
Trong ngôn ngữ toán học, ta có thể mô phỏng cấu trúc này bằng một Hỗn hợp Gauss hạng thấp, gọi là MoLRG. Thay vì là một đám mây khối cầu khổng lồ trong không gian $d$ chiều, dữ liệu thực chất tụ tập lại quanh những mặt phẳng mỏng manh $U_i$. Nhiệm vụ của quá trình học không còn là lấp đầy không gian quá rộng, mà là định vị được các mặt phẳng này."