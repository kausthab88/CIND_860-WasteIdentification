
# Project Title: Automated Waste Material Categorization Using Computer Vision Techniques

I. Introduction

(a) Problem Context and Chosen Theme

The escalating volume of global waste, with over 2 billion tons generated annually [World Bank, 2022], poses a substantial challenge to waste management systems. Landfills are under increasing strain, emphasizing the critical need for innovative solutions. This project focuses on leveraging computer vision techniques to automate the identification and categorization of diverse waste materials. The chosen theme revolves around the application of artificial intelligence, specifically computer vision, to streamline the waste segregation process.

II. Problem Statement

(b) Problem Addressed and Research Questions

The manual effort and time required by trash separators to categorize diverse waste materials in landfills are significant, contributing to operational inefficiencies. The research questions of this project are:

•	How can computer vision techniques be optimized to accurately identify and categorize a diverse range of waste materials based on visual cues?
•	What is the feasibility and effectiveness of extending the automated waste categorization solution to domestic households to improve waste segregation practices?
•	How can real-time data collection on-site contribute to the adaptability and robustness of the computer vision model in handling dynamic waste compositions?

III. Overall Methodology

The methodology adopted for this project was structured to systematically address the challenge of enhancing the accuracy of waste material categorization using computer vision techniques. This approach involved several distinct phases: literature review, dataset selection and preparation, model replication and enhancement, and evaluation. Each phase played a critical role in the project's development and execution, as outlined below:

**Literature Review:**

The initial phase of the project entailed a comprehensive literature review aimed at understanding the current landscape of computer vision applications within waste management. This review focused on identifying previous methodologies, the types of models built, and the common challenges encountered in similar projects. By examining a wide range of research papers and case studies, the review provided a solid foundation for the project, highlighting successful strategies and areas needing improvement. This phase was crucial for informing the subsequent steps, ensuring that the project was built on a solid base of existing knowledge and best practices.


**Dataset Selection and Preparation:**

Based on insights gained from the literature review, the RealWaste dataset was selected for its relevance and applicability to the project's objectives. This dataset, comprising images of various waste materials, provided the raw material for model training and testing. Given the computational constraints encountered, particularly the limitations posed by Google Colab's resources, the dataset was meticulously curated. This involved downsizing the original set from around 4800 images to 2500, ensuring a manageable volume while retaining a representative mix of waste material types. The preparation phase also included data cleaning and augmentation procedures to enhance model training effectiveness.

**Model Replication and Enhancement:**

With the dataset prepared, the next phase involved replicating existing computer vision models identified during the literature review. The initial replication focused on a default Convolutional Neural Network (CNN) utilizing VGG16 layers, selected for its prominence in similar research and applicability to image recognition tasks. Following the replication, the project moved into an enhancement phase, aiming to address the limitations and challenges identified in the replicated models. This phase included a series of iterative improvements, such as tuning hyperparameters (e.g., adjusting learning rates and batch sizes) and implementing data augmentation techniques. These enhancements were geared towards improving the model's ability to generalize from training data to unseen test data, thereby increasing accuracy and reducing overfitting.

**Evaluation:**

The final phase of the methodology involved a rigorous evaluation of the enhanced models. This entailed comparing the performance of the models before and after the enhancement interventions, with a focus on metrics such as accuracy, precision, and recall. The evaluation aimed to assess the effectiveness of the enhancements in improving the models' ability to accurately categorize waste materials. This phase was critical for validating the project's objectives and providing a clear measure of the progress made through the project's interventions.

Throughout the project, the methodology adhered to principles of rigorous scientific research, ensuring that each step was carefully planned, executed, and evaluated. By following this structured approach, the project aimed to contribute meaningful advancements to the field of waste management through the application of computer vision techniques.
