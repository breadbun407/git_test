public class Book
{
    // Properties
    public string Title { get; set; }
    public string Author { get; set; }
    public DateTime PublicationDate { get; set; }
    public string ISBN { get; set; }

    // Constructor
    public Book(string title, string author, DateTime publicationDate, string isbn)
    {
        Title = title;
        Author = author;
        PublicationDate = publicationDate;
        ISBN = isbn;
    }

    // Method to display book information
    public void DisplayInfo()
    {
        Console.WriteLine($"Title: {Title}");
        Console.WriteLine($"Author: {Author}");
        Console.WriteLine($"Publication Date: {PublicationDate}");
        Console.WriteLine($"ISBN: {ISBN}");
        Console.WriteLine();
    }
}
