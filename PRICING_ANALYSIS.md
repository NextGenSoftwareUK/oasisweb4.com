# Pricing Analysis: Main API vs MCP Server

## Current Pricing Comparison

### Main OASIS API Pricing
- **Bronze**: $9/month - 10,000 API requests, 1 GB storage
- **Silver**: $29/month - 100,000 API requests, 10 GB storage  
- **Gold**: $99/month - 1,000,000 API requests, 100 GB storage
- **Enterprise**: Custom - Unlimited

### MCP Server Pricing
- **14-Day Trial**: Free - Unlimited API calls
- **Free**: $0/month - 100 API calls
- **Starter**: $29/month - 1,000 API calls
- **Professional**: $99/month - 10,000 API calls

## Issues Identified

### 1. **Massive Discrepancy in API Limits**

**Problem:** MCP Server pricing is 100x more restrictive than main API pricing at the same price points:

- **$29 tier:**
  - Main API Silver: 100,000 calls
  - MCP Starter: 1,000 calls
  - **Difference: 100x less**

- **$99 tier:**
  - Main API Gold: 1,000,000 calls
  - MCP Professional: 10,000 calls
  - **Difference: 100x less**

### 2. **Conceptual Confusion**

The MCP Server is just a **client interface** to the OASIS API. It doesn't provide separate infrastructure or services - it's a tool that makes API calls on behalf of the user.

**Question:** Should MCP have separate pricing, or should it use the same API limits as the main API subscription?

### 3. **Missing Bronze Tier**

Main API has a $9 Bronze tier, but MCP doesn't offer this option.

## Recommendations

### Option A: Align MCP with Main API (Recommended)

**MCP Server should use the same pricing tiers as the main API:**

- **14-Day Trial**: Free - Full access (no credit card)
- **Free**: $0/month - 100 API calls (same as now)
- **Bronze**: $9/month - 10,000 API calls (matches main API)
- **Silver**: $29/month - 100,000 API calls (matches main API)
- **Gold**: $99/month - 1,000,000 API calls (matches main API)
- **Enterprise**: Custom - Unlimited

**Benefits:**
- Consistent pricing across all OASIS products
- Users understand they're getting the same API access
- Simpler to explain and market
- No confusion about "which subscription do I need?"

### Option B: MCP as Add-On Service

If MCP is meant to be a premium developer tool:

- **MCP Access**: $X/month (one-time fee for the tool)
- **API Usage**: Uses your existing OASIS API subscription limits
- **Example**: "MCP Server access: $9/month + your API subscription"

**Benefits:**
- Separates tool access from API usage
- Users can use MCP with any API tier
- Clear value proposition for the developer tool

### Option C: Unified Subscription

**Single subscription covers both API access and MCP Server:**

- One subscription = API access + MCP Server access
- Same pricing tiers as main API
- MCP is included as a feature, not separate product

**Benefits:**
- Simplest for users
- No confusion about what they're paying for
- MCP becomes a value-add, not separate product

## Recommended Solution

**Option A (Align MCP with Main API)** is recommended because:

1. **Consistency**: Users expect the same limits regardless of how they access the API
2. **Simplicity**: One pricing model, easy to understand
3. **Fairness**: Same price = same limits, whether using API directly or via MCP
4. **Marketing**: "Access OASIS via API or MCP - same subscription, same limits"

## Updated MCP Pricing Structure

```
14-Day Trial: Free
├─ Unlimited API calls
├─ All features
└─ No credit card required

Free: $0/month
├─ 100 API calls/month
├─ Read-only operations
└─ Community support

Bronze: $9/month
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

## Action Items

1. ✅ Update MCP pricing to match main API tiers
2. ✅ Add Bronze tier ($9/month) to MCP
3. ✅ Update API call limits to match main API
4. ✅ Clarify that MCP uses the same API subscription
5. ✅ Update marketing copy to reflect unified pricing
