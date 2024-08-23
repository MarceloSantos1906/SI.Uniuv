import type { FastifyInstance } from "fastify";
import type { ZodTypeProvider } from "fastify-type-provider-zod";
import { z } from "zod";
import { prisma } from "../../lib/prisma";
import dayjs from "dayjs";

export async function registerBook(app: FastifyInstance) {
	app.withTypeProvider<ZodTypeProvider>().post('/registerBook', {
		schema: {
			body: z.object({
				name: z.string().min(1),
				genres: z.array(z.string().min(1)),
				authors: z.array(z.string().min(1)),
				publisher: z.string().min(1),
				publish_date: z.coerce.date()
			})
		}
	}, async (req) => {
		const { name, publisher, publish_date, genres, authors } = req.body

		if (dayjs(publish_date).isAfter(new Date())) {
			throw new Error('Invalid publish date.')
		}

		const book = await prisma.books.create({
			data: {
				name,
				publisher,
				publish_date,
				genres: {
					createMany: {
						data: [{
							
						}]
					}
				},
				authors: ""
			},
			})
		return { bookId: book.booksId }
	})
}