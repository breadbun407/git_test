using System;
using System.Windows.Forms;

public class BookStorageForm : Form
{
    // Constructor
    public BookStorageForm()
    {
        InitializeComponent();
    }

    // Entry point
    [STAThread]
    static void Main()
    {
        Application.EnableVisualStyles();
        Application.Run(new BookStorageForm());
    }

    // Initialize the form and its components
    private void InitializeComponent()
    {
        // Set properties of the form
        this.Text = "Book Storage Application";
        this.Size = new System.Drawing.Size(800, 600);
        
        // Create controls
        var titleLabel = new Label();
        titleLabel.Text = "Title:";
        titleLabel.Location = new System.Drawing.Point(20, 20);
        titleLabel.Size = new System.Drawing.Size(80, 20);

        var titleTextBox = new TextBox();
        titleTextBox.Location = new System.Drawing.Point(120, 20);
        titleTextBox.Size = new System.Drawing.Size(200, 20);

        var saveButton = new Button();
        saveButton.Text = "Save";
        saveButton.Location = new System.Drawing.Point(20, 60);
        saveButton.Size = new System.Drawing.Size(80, 30);
        saveButton.Click += SaveButton_Click;

        // Add controls to the form
        this.Controls.Add(titleLabel);
        this.Controls.Add(titleTextBox);
        this.Controls.Add(saveButton);
    }

    // Event handler for save button click
    private void SaveButton_Click(object sender, EventArgs e)
    {
        // Add your code here to handle the save button click event
    }
}

