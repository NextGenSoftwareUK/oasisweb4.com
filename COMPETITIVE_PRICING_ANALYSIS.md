# Competitive Pricing Analysis: OASIS vs Market

## Executive Summary

After researching similar products, OASIS pricing shows **both alignment and misalignment** with market standards. Key findings:

✅ **Well-aligned:**
- Free tier and trial options
- Tiered pricing structure
- Clear feature differentiation

⚠️ **Needs adjustment:**
- MCP pricing is 100x more restrictive than main API at same price points
- Missing Bronze tier ($9) in MCP
- Pricing inconsistency between products

## Market Benchmarks

### 1. AI/Developer Tool Pricing (2025)

| Product | Entry Tier | Mid Tier | Premium Tier | Model |
|---------|-----------|----------|--------------|-------|
| **ChatGPT Plus** | $20/month | - | $200/month (Pro) | Individual + Power User |
| **Claude Pro** | $20/month | - | $100-200/month | Individual + Power User |
| **Grok Premium+** | $22/month | - | Higher tiers | Individual + API |
| **General SaaS Tools** | $10-40/month | $40-100/month | $100-200+/month | Freemium + Tiered |

**Key Insight:** $20-30/month is the "sweet spot" for individual Pro users.

### 2. Blockchain/Web3 API Pricing

| Product | Free Tier | Starter | Growth | Enterprise |
|---------|-----------|---------|--------|------------|
| **Alchemy** | Limited requests | ~$49/month | ~$149/month | Custom |
| **Infura** | 100k requests/day | ~$50/month | ~$200/month | Custom |
| **QuickNode** | Limited | ~$49/month | ~$299/month | Custom |
| **Moralis** | Free tier | ~$49/month | ~$149/month | Custom |

**Key Insight:** Blockchain APIs typically start at $49/month for paid tiers, with generous free tiers.

### 3. API Management Platforms

| Product | Free Tier | Basic | Standard | Premium |
|---------|-----------|-------|----------|---------|
| **Azure API Management** | Limited | Basic tier | Standard tier | Premium tier |
| **APIVerve** | Free credits | Starter | Pro | Mega |
| **SendGrid** | Free tier | $19.95/month | Higher tiers | Enterprise |

**Key Insight:** Most APIs offer:
- Generous free tiers (100k-1M requests)
- Starter tiers around $20-50/month
- Clear usage-based limits

### 4. MCP-Specific Products

| Product | Free Tier | Starter | Pro | Enterprise |
|---------|-----------|---------|-----|------------|
| **Supermachine.ai** | Limited | ~$99/month | ~$499/month | Custom |
| **Ninja.ai** | Limited | $19/user/month | $99/user/month | Custom |
| **MCP-Builder.ai** | Free tier | $25/month | $50/month | Custom |
| **Code Studio** | Free | ~$20/user/month | ~$30/user/month | Higher |

**Key Insight:** MCP products typically start at $20-100/month, with free tiers for testing.

### 5. Developer Tool Pricing Patterns

**Common Structure:**
1. **Free/Trial**: Limited usage, basic features
2. **Starter/Developer**: $10-50/month, moderate limits
3. **Pro/Growth**: $50-150/month, higher limits, better support
4. **Enterprise**: Custom pricing, unlimited, SLAs

**Usage Limits Pattern:**
- Free: 10k-100k requests/month
- Starter: 100k-1M requests/month
- Pro: 1M-10M requests/month
- Enterprise: Unlimited

## OASIS Current Pricing Analysis

### Main OASIS API
- **Bronze**: $9/month - 10,000 requests ✅ (Below market, good value)
- **Silver**: $29/month - 100,000 requests ✅ (Aligned with market)
- **Gold**: $99/month - 1,000,000 requests ✅ (Aligned with market)
- **Enterprise**: Custom - Unlimited ✅

**Verdict:** Main API pricing is **well-aligned** with market standards.

### MCP Server (Current)
- **Free**: $0/month - 100 requests ⚠️ (Very restrictive)
- **Starter**: $29/month - 1,000 requests ❌ (100x less than main API)
- **Professional**: $99/month - 10,000 requests ❌ (100x less than main API)

**Verdict:** MCP pricing is **severely misaligned** and inconsistent.

## Competitive Comparison

### OASIS vs RefineAPI (API Service)

| Tier | RefineAPI | OASIS Main API | OASIS MCP |
|------|-----------|----------------|-----------|
| Free | 100 requests | 100 calls | 100 calls |
| Starter | $9/month (1k requests) | $9/month (10k calls) | $29/month (1k calls) |
| Pro | $39/month (10k requests) | $29/month (100k calls) | $99/month (10k calls) |

**Finding:** OASIS main API offers **10x more value**. MCP is **way off**.

### OASIS vs Alchemy (Blockchain API)

| Tier | Alchemy | OASIS Main API | OASIS MCP | Verdict |
|------|---------|----------------|-----------|---------|
| Free | Limited | 100 calls | 100 calls | Similar |
| Starter | ~$49 | $9 (Bronze) | $29 (1k calls) | OASIS cheaper, but MCP restrictive |
| Growth | ~$149 | $29 (Silver) | $99 (10k calls) | OASIS better value, MCP way off |
| Enterprise | Custom | Custom | - | Similar |

**Finding:** OASIS main API is **more competitive** than Alchemy. MCP is **way off**.

### OASIS vs GitHub Copilot (IDE Tool)

| Tier | GitHub Copilot | OASIS Main API | OASIS MCP |
|------|----------------|----------------|-----------|
| Free | 2k completions/month | 100 calls | 100 calls |
| Entry | $10/month | $9/month | $29/month (1k calls) |
| Pro | $39/month | $29/month | $99/month (10k calls) |

**Finding:** OASIS main API is **cheaper** than Copilot. MCP pricing is **inconsistent**.

### OASIS vs ChatGPT/Claude (AI Tools)

| Tier | ChatGPT/Claude | OASIS Main API | OASIS MCP |
|------|----------------|----------------|-----------|
| Entry | $20/month | $9/month | $29/month (1k calls) |
| Pro | $100-200/month | $29/month | $99/month (10k calls) |

**Finding:** OASIS is **much cheaper** than AI tools, but MCP pricing doesn't reflect this value.

## Market Alignment Score

### Main OASIS API: ✅ 9/10
- **Strengths:**
  - Competitive pricing vs blockchain APIs
  - Clear tier structure
  - Good free tier
  - Bronze tier ($9) is excellent value
  
- **Weaknesses:**
  - Could add more tiers between $29 and $99

### MCP Server: ❌ 3/10
- **Strengths:**
  - Has free tier
  - Has trial option
  
- **Weaknesses:**
  - 100x more restrictive than main API at same price
  - Missing Bronze tier
  - Inconsistent with main API
  - Doesn't align with market standards

## Recommendations

### 1. Align MCP with Main API (CRITICAL)

**Current Problem:**
- MCP Starter ($29) = 1,000 calls
- Main API Silver ($29) = 100,000 calls
- **100x difference!**

**Solution:** Make MCP use same pricing as main API:
- MCP is just a client interface
- Should share the same subscription
- Users expect consistency

### 2. Add Bronze Tier to MCP

**Current:** Missing $9 tier
**Market Standard:** Most products have entry tier around $10-20
**Recommendation:** Add Bronze tier to match main API

### 3. Update Pricing Structure

**Recommended MCP Pricing:**

```
14-Day Trial: Free
├─ Unlimited API calls
├─ All features
└─ No credit card required

Free: $0/month
├─ 100 API calls/month
├─ Read-only operations
└─ Community support

Bronze: $9/month (NEW)
├─ 10,000 API calls/month
├─ 1 GB storage
├─ All read operations
└─ Community support

Silver: $29/month (Popular)
├─ 100,000 API calls/month
├─ 10 GB storage
├─ All operations
├─ Priority processing
└─ Email support

Gold: $99/month
├─ 1,000,000 API calls/month
├─ 100 GB storage
├─ All features
├─ Advanced analytics
└─ Priority support

Enterprise: Custom
├─ Unlimited API calls
├─ Unlimited storage
├─ Custom integrations
├─ SLA & SSO
└─ Dedicated support
```

### 4. Market Positioning

**Main API:** ✅ Already well-positioned
- More competitive than Alchemy/Infura
- Better value than AI tools
- Clear tier structure

**MCP Server:** Needs repositioning
- Should be positioned as "same API, better interface"
- Not a separate product with separate limits
- Value proposition: "Access OASIS via IDE - same subscription"

## Competitive Advantages

After alignment, OASIS will have:

1. **Better Value than Blockchain APIs**
   - OASIS: $9 for 10k calls
   - Alchemy: $49 for similar
   - **5x better value**

2. **More Competitive than AI Tools**
   - OASIS: $29 for 100k calls
   - ChatGPT: $20 for limited usage
   - **Better value for developers**

3. **Consistent Pricing**
   - Same limits whether using API directly or via MCP
   - Builds trust and clarity

## Action Items

1. ✅ **Update MCP pricing** to match main API
2. ✅ **Add Bronze tier** ($9/month) to MCP
3. ✅ **Update marketing copy** to clarify MCP uses same subscription
4. ✅ **Update pricing page** to show unified pricing
5. ✅ **Test pricing** with beta users

## Conclusion

**Main OASIS API pricing is excellent** and well-aligned with market standards.

**MCP Server pricing needs immediate alignment** with the main API to:
- Maintain consistency
- Build trust
- Reflect actual value
- Compete effectively

The recommended changes will make OASIS **more competitive** than most blockchain APIs while maintaining **better value** than AI tools.
