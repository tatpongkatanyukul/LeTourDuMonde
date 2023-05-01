# Around the World of Compuation in in 80+ Python Programs

# Short description

A dual-language book for curiosity and spirit of adventures.

---

# คำนำ 

หนังสือเล่มนี้รวบรวมโจทย์ปัญหาการเขียนโปรแกรมคอมพิวเตอร์ โดยโจทย์มีความหลากหลายเกี่ยวพันกับหลากหลายศาสตร์ ซึ่งหวังว่าทำให้เกิดการเรียนรู้แบบขยาย (divergent learning) ช่วยเสริมสร้างความคิดสร้างสรรค์ ได้โอกาสทบทวนศาสตร์อื่น ๆ และ/หรือได้เรียนรู้เรื่องใหม่ ๆ ที่อาจยังไม่เคยเรียนรู้มาก่อน เกิดความใฝ่รู้ เกิดแรงบันดาลใจ และช่วยพัฒนาทั้งทักษะการแก้ปัญหาและทักษะการเรียนรู้ และที่สำคัญทำให้สนุก

อย่างไรก็ตาม เรามองโลกจากจุดที่เรายืน โจทย์ต่าง ๆ ที่รวบรวมมานี้ได้ดั่งเดิมเขียนขึ้นสำหรับนักศึกษาวิศวกรรมคอมพิวเตอร์หลาย ๆ ชั้นปีในระดับปริญญาตรี มหาวิทยาลัยขอนแก่น และผู้เขียนก็หวังว่า สิ่งที่ทำนี้จะเป็นประโยชน์แก่ผู้อ่านทั่วไปบ้างไม่มากก็น้อย

ผู้เขียนขอออกตัวก่อนว่า ความหลากหลายเป็นทั้งโอกาสและความเสี่ยง ถึงแม้ผู้เขียนจะพยายามให้เนื้อหามีความถูกต้องและสมบูรณ์ แต่บางครั้งอาจจะด้วยความเหมาะสมของเนื้อหาหรืออาจจะด้วยความรู้ความเข้าใจความสามารถที่จำกัดของผู้เขียนเอง อาจทำให้ความรู้ของเรื่องราวที่เกี่ยวข้องบางอย่างคลาดเคลื่อนไป ผู้เขียนก็ขออภัยในกรณีนี้ด้วย

แต่สำคัญกว่าความสมบูรณ์แบบ คือความกล้าที่จะทำเรื่องที่ไม่เคยทำมาก่อน ความเห็นอกเห็นใจที่จะพยายามเข้าใจในคนอื่นศาสตร์อื่น ความเมตตาที่จะให้อภัยกับตัวเองเวลาที่ทำผิด เวลาที่เรียนรู้ได้ช้า และปัญญาที่มองเห็นประโยชน์ในภาพใหญ่ และหวังว่าหนังสือเล่มจะมีส่วนในคุณธรรมเหล่านี้

อีกเรื่องที่ควรออกตัว คือ หนังสือเล่มนี้ไม่ได้เขียนขึ้นเพื่อเป็นหนังสือเล่มแรกที่จะสอนการเขียนโปรแกรม แต่ทำหน้าที่เสริมความรู้ความเข้าใจด้วยแบบฝึกหัดที่หลากหลาย ดังนั้นทฤษฎีหากมีจะเป็นเพียงการทบทวนสั้น ๆ คำใบ้ หรือเกร็ดความรู้เท่านั้น 

# Preface

This book offers diverse programming problems involving a wide range of subjects. This approach is expected to promote divergent learning, boost creativity, review what readers have learned in other fields, teach what they have not, invoke curiosity, inspire, improve both problem solving and learning skills and have fun.  

However, we see the world from where we stand. Problems presented here have been written for computer engineering undergraduates of Khon Kaen University. I believe that it can also be beneficial to other readers.

The first thing I need to get it out is that diversity brings both opportunity and risk. Despite doing my best, there might be intellectual mistakes due to either intended simplification or my own limitation on the subjects. I would like to apologize if that is the case.

Anyhow, a bigger goal than perfection is to convey courage to take on a challenge, empathy to learn others’ points, compassion to be kind to ourselves, our mistake, and our underperformance, and wisdom to see benefits in a big picture. Hopefully, this book will contribute to these qualities.

Another thing is that this book is not intended to be the first programming book. Instead, it is expected to complement with variety of exercises. Therefore, it does not provide a full treatment on programming materials, but possibly brief reviews, hints, or tidbits.

---
# Title

* ท่องรอบโลกการคำนวณใน 80+ ไพธอนโปรแกรม
* Around the World of Computation in 80+ Python Programs

ปล 80+ จำนวนโปรแกรมนะครับ ไม่ได้จำกัดอายุคนอ่าน

---

Status: under preparation! (Started project in Apr 2023)

Expected to finish: I don't know, before I retire! (I hope.)

* [Handouts](https://github.com/tatpongkatanyukul/LeTourDuMonde/tree/main/handouts)
* [Solutions](https://github.com/tatpongkatanyukul/LeTourDuMonde/tree/main/code)
* Errata

---

# Resources

* Filenaming convention (2023, May 1)
  * Since there will be a lot of resource files, e.g., codes, figures, data, it may be easier to establish a convention for filenames.
    1. Some files I have uploaded before this convention.
    2. Some I may forget (or be too lazy) to do it.
  * It's better to have a prefix then ```{prefix}_{title}```
    * Title can be anything, meaningful if possible.
    * Prefix
      * ```ee{c}```: electricity and electromagnetism
      * ```en{c}```: engineering (outside traditional ee)
      * ```sh{c}```: short / miscellaneous / wider topic (outside traditional en or ee)      
      * ```{c}```: course code: since all problems I'll take them from course exercises/homeworks, I can add this so that it helps me trace it.
        * ```{c}```: ```lca``` or ```lca{y}{L}{P}```, e.g., ```lca2022L01P8``` for P8 of Lab01 for lca class of 2022.
        * Similarly, ```iml```, ```ann```, ```ai```, or ```book``` for a problem written particularly for the book
    * Example, ```eelca2024L3P12_circularloop.png```
        
