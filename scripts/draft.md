### Scene 3: La bàn trong không gian nhiễu (2:20 - 3:35)
**Mục tiêu:** Nhắc lại toán học cốt lõi (SDE, ODE, Score function).

* **[2:20 - 2:45] Manim Visual:** Xóa cảnh cũ. Đặt một `Dot` đại diện cho $x_0$. Dùng một `ValueTracker` kết hợp `TracedPath` để vẽ một quỹ đạo chuyển động Brown hỗn loạn (Forward process) biến $x_0$ thành $x_T$. Dùng `MathTex` hiện phương trình: $dx = f(x,t)dt + g(t)dw$.
* **[2:45 - 3:10] Manim Visual:** Dùng `TransformMatchingTex` biến đổi mượt mà SDE thuận thành ODE lùi (Probability Flow ODE). Giữ nguyên các ký tự chung để tạo sự liên kết thị giác:
    $$dx = \left[ f(x, t) - \frac{1}{2}g(t)^2 \nabla_x \log p_t(x) \right] dt$$
* **[3:10 - 3:35] Manim Visual:** Dùng `set_color` tô vàng cụm $\nabla_x \log p_t(x)$. Chuyển cảnh sang một `VectorField`, trong đó các vector gradient đều hướng về các điểm dữ liệu mật độ cao.

**[Voiceover]**

"Để giải mã bí ẩn này, hãy nhìn lại gốc rễ của quá trình khuếch tán. Một điểm dữ liệu ban đầu sẽ trải qua một quá trình tản mạn ngẫu nhiên, trôi dạt vô định theo phương trình vi phân ngẫu nhiên, hay SDE này.
Nhưng vẻ đẹp của toán học nằm ở tính khả nghịch. Quá trình sinh ảnh thực chất là việc đi ngược lại quỹ đạo đó, tuân theo một phương trình vi phân thường — Probability Flow ODE. 
Hãy chú ý vào cụm vi phân này: Score Function. Trong một không gian mênh mông nhiễu loạn, đại lượng này chính là một chiếc la bàn. Nó tạo ra một trường vector, luôn chỉ hướng về nơi có mật độ dữ liệu thực cao nhất. 
Mục tiêu duy nhất của mạng nơ-ron là xấp xỉ chiếc la bàn này. Nhưng vấn đề là: không gian hình ảnh chứa hàng triệu chiều. Làm sao một mô hình có thể xấp xỉ chính xác một trường vector lớn như vậy mà không dính phải lời nguyền của chiều dữ liệu?"