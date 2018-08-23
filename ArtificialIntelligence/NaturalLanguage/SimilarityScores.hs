-- https://www.hackerrank.com/challenges/nlp-similarity-scores/problem
-- DONE

module Main where

    d1 :: String
    d1 = "I'd like an apple"
    
    d2 :: String
    d2 = "An apple a day keeps the doctor away"
    
    d3 :: String
    d3 = "Never compare an apple to an orange"
    
    d4 :: String
    d4 = "I prefer scikit-learn to orange"

    d = [d1, d2, d3, d4]
    

    tf :: Fractional a => String -> String -> a
    tf term document = fromIntegral termCount / fromIntegral (length docArr)
        where
            docArr = words document
            termCount = length $ filter (== term) docArr 

    idf :: Floating a => String -> [String] -> a
    idf term corpus = 1 + logBase 2.7 (fromIntegral (length corpus) / fromIntegral (ocurrences corpus term 0))
        where
            ocurrences corpus term counter
                | length corpus == 0 = counter
                | term `elem` words (head corpus) = ocurrences (tail corpus) term (counter + 1)
                | otherwise = ocurrences (tail corpus) term counter


    tfidf :: Floating a => String -> String -> [String] -> a
    tfidf term document corpus = (tf term document) * (idf term corpus)


    ----------------------------------------------------------------------------------------------------
    documentSimilarity :: Floating a => String -> [String] -> a -> a
    documentSimilarity document term score
        | length term == 0 = score
        | otherwise = documentSimilarity document (tail term) (score + (tfidf (head term) document d))

      
    similarities :: [Double]
    similarities = [0,0] ++ [documentSimilarity document (words document) 0 | document <- [d2, d3, d4]]

    maxIndex xs = head $ filter ((== maximum xs) . (xs !!)) [0..]

    main :: IO()
    main = print $ maxIndex similarities
    