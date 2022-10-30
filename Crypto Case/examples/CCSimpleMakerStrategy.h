#pragma once
#include "strategies/CCModelStrategy.h"
#include "components/NotificationManager.h"

using namespace cts;
using namespace std;

class CCSimpleMakerStrategy: public CCModelStrategy {
public:
	using CCModelStrategy::CCModelStrategy;
	void init() override;

protected:
	void tradeOnSignal(double signal) override;
	void maintainOrders(TradeDirs side, double tgtPx, bool allowNewOrder=false);
	bool placeNewOrder(TradeDirs side, double tgtPx);
	double calc_desired_order_qty(double px, TradeDirs side);
	double calcQuotePrice(TradeDirs side, double spds=1.0);
	double getMakeMidpx();

protected:
	NotificationManager* _notMgr;
	double _quote_spread;
	double _safe_quote_distance;
	double _max_quote_error;
	double _max_quote_signal_diff;
	PricingModel * _makeMidPm;
};
