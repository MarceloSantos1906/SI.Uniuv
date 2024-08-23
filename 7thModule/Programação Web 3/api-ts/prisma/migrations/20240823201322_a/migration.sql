-- CreateTable
CREATE TABLE "books" (
    "booksId" TEXT NOT NULL PRIMARY KEY,
    "name" TEXT NOT NULL,
    "publisher" TEXT NOT NULL,
    "publish_date" DATETIME NOT NULL,
    "registered_at" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- CreateTable
CREATE TABLE "genres" (
    "genreId" TEXT NOT NULL PRIMARY KEY,
    "genre" TEXT NOT NULL,
    "registerDate" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- CreateTable
CREATE TABLE "authors" (
    "authorId" TEXT NOT NULL PRIMARY KEY,
    "name" TEXT NOT NULL,
    "registerDate" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- CreateTable
CREATE TABLE "_BooksToGenres" (
    "A" TEXT NOT NULL,
    "B" TEXT NOT NULL,
    CONSTRAINT "_BooksToGenres_A_fkey" FOREIGN KEY ("A") REFERENCES "books" ("booksId") ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT "_BooksToGenres_B_fkey" FOREIGN KEY ("B") REFERENCES "genres" ("genreId") ON DELETE CASCADE ON UPDATE CASCADE
);

-- CreateTable
CREATE TABLE "_AuthorsToBooks" (
    "A" TEXT NOT NULL,
    "B" TEXT NOT NULL,
    CONSTRAINT "_AuthorsToBooks_A_fkey" FOREIGN KEY ("A") REFERENCES "authors" ("authorId") ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT "_AuthorsToBooks_B_fkey" FOREIGN KEY ("B") REFERENCES "books" ("booksId") ON DELETE CASCADE ON UPDATE CASCADE
);

-- CreateIndex
CREATE UNIQUE INDEX "_BooksToGenres_AB_unique" ON "_BooksToGenres"("A", "B");

-- CreateIndex
CREATE INDEX "_BooksToGenres_B_index" ON "_BooksToGenres"("B");

-- CreateIndex
CREATE UNIQUE INDEX "_AuthorsToBooks_AB_unique" ON "_AuthorsToBooks"("A", "B");

-- CreateIndex
CREATE INDEX "_AuthorsToBooks_B_index" ON "_AuthorsToBooks"("B");
