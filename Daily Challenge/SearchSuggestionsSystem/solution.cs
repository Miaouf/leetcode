public class Solution {
    public IList<IList<string>> SuggestedProducts(string[] products, string searchWord) {
        IList<IList<string>> res = new List<IList<string>>();
        List<string> productsFormatted = new List<string>(products);
        productsFormatted.Sort();
        int len = searchWord.Length;
        for (int i = 0; i < len; i++ )
        {
            /* Using temporary list to compute the primary one */
            List<string> loopList = new List<string>();
            loopList.AddRange(productsFormatted);
            /* looping on temporary list */
            foreach(string product in loopList)
            {
                /* we remove each product which not start with the current search string */
                if (!product.StartsWith(searchWord.Substring(0,i+1)))
                {
                    productsFormatted.Remove(product);
                }
            }
            /* Now we need to extract the first 3 first strings that match the current search string */
            List<string> current = new List<string>();
            int last = (3 <= productsFormatted.Count)?3:(2 == productsFormatted.Count)?2:(1 == productsFormatted.Count)?1:0;
            current = productsFormatted.GetRange(0, last);
            res.Add(current);
        }
        return res;
    }
}
